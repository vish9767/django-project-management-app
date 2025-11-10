from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from django.db.models import Sum, Count, Avg, Q
from django.utils import timezone
from datetime import timedelta
import requests
import random
import urllib3

# Suppress SSL warnings for demo purposes (not recommended for production)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from .models import Project, Task
from .serializers import ProjectSerializer, ProjectListSerializer, TaskSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing project instances.
    Provides CRUD operations: list, create, retrieve, update, delete
    """
    queryset = Project.objects.all()
    
    def get_serializer_class(self):
        """Use different serializers for list and detail views"""
        if self.action == 'list':
            return ProjectListSerializer
        return ProjectSerializer
    
    def list(self, request):
        """List all projects with optional filtering"""
        queryset = self.get_queryset()
        
        # Filter by status if provided
        status_filter = request.query_params.get('status', None)
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        
        # Filter by client name if provided
        client_filter = request.query_params.get('client', None)
        if client_filter:
            queryset = queryset.filter(client_name__icontains=client_filter)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'count': queryset.count(),
            'results': serializer.data
        })
    
    def create(self, request):
        """Create a new project"""
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        """Retrieve a specific project with all its tasks"""
        try:
            project = self.get_queryset().get(pk=pk)
            serializer = ProjectSerializer(project)
            return Response(serializer.data)
        except Project.DoesNotExist:
            return Response(
                {'error': 'Project not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )
    
    def update(self, request, pk=None, partial=False):
        """Update a project (supports both PUT and PATCH)"""
        try:
            project = self.get_queryset().get(pk=pk)
            serializer = ProjectSerializer(project, data=request.data, partial=partial)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Project.DoesNotExist:
            return Response(
                {'error': 'Project not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )
    
    def destroy(self, request, pk=None):
        """Delete a project"""
        try:
            project = self.get_queryset().get(pk=pk)
            project.delete()
            return Response(
                {'message': 'Project deleted successfully'}, 
                status=status.HTTP_204_NO_CONTENT
            )
        except Project.DoesNotExist:
            return Response(
                {'error': 'Project not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )


class TaskViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing task instances.
    Provides CRUD operations for tasks
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    def list(self, request):
        """List all tasks with optional filtering"""
        queryset = self.get_queryset()
        
        # Filter by project if provided
        project_id = request.query_params.get('project', None)
        if project_id:
            queryset = queryset.filter(project_id=project_id)
        
        # Filter by completion status
        completed = request.query_params.get('completed', None)
        if completed is not None:
            queryset = queryset.filter(completed=completed.lower() == 'true')
        
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'count': queryset.count(),
            'results': serializer.data
        })


@api_view(['GET'])
def dashboard_stats(request):
    """
    Data visualization endpoint showing project statistics and insights.
    This demonstrates the reporting/visualization requirement.
    """
    # Calculate overall statistics
    total_projects = Project.objects.count()
    total_budget = Project.objects.aggregate(Sum('budget'))['budget__sum'] or 0
    avg_budget = Project.objects.aggregate(Avg('budget'))['budget__avg'] or 0
    
    # Status breakdown
    status_breakdown = {}
    for status_choice, _ in Project._meta.get_field('status').choices:
        count = Project.objects.filter(status=status_choice).count()
        status_breakdown[status_choice] = count
    
    # Tasks statistics
    total_tasks = Task.objects.count()
    completed_tasks = Task.objects.filter(completed=True).count()
    completion_rate = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
    
    # Recent projects (last 30 days)
    thirty_days_ago = timezone.now().date() - timedelta(days=30)
    recent_projects = Project.objects.filter(created_at__gte=thirty_days_ago).count()
    
    # Projects by client
    projects_by_client = Project.objects.values('client_name').annotate(
        project_count=Count('id'),
        total_budget=Sum('budget')
    ).order_by('-project_count')[:5]
    
    # Task priority breakdown
    priority_breakdown = {}
    for priority_choice, _ in Task._meta.get_field('priority').choices:
        count = Task.objects.filter(priority=priority_choice).count()
        priority_breakdown[priority_choice] = count
    
    return Response({
        'overview': {
            'total_projects': total_projects,
            'total_budget': float(total_budget),
            'average_budget': float(avg_budget),
            'recent_projects_30_days': recent_projects,
        },
        'project_status': status_breakdown,
        'tasks': {
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'pending_tasks': total_tasks - completed_tasks,
            'completion_rate': round(completion_rate, 2),
        },
        'priority_distribution': priority_breakdown,
        'top_clients': list(projects_by_client),
    })


@api_view(['GET'])
def fetch_external_data(request):
    """
    Third-party API integration example.
    Fetches random quotes from a public API to demonstrate external API integration.
    Falls back to local quotes if external API fails.
    """
    # Fallback quotes in case API fails
    fallback_quotes = [
        {
            'content': 'The only way to do great work is to love what you do.',
            'author': 'Steve Jobs',
            'tags': ['inspiration', 'work', 'passion']
        },
        {
            'content': 'Innovation distinguishes between a leader and a follower.',
            'author': 'Steve Jobs',
            'tags': ['innovation', 'leadership']
        },
        {
            'content': 'Success is not final, failure is not fatal: it is the courage to continue that counts.',
            'author': 'Winston Churchill',
            'tags': ['success', 'courage', 'perseverance']
        },
        {
            'content': 'The future belongs to those who believe in the beauty of their dreams.',
            'author': 'Eleanor Roosevelt',
            'tags': ['dreams', 'future', 'inspiration']
        },
        {
            'content': 'Code is like humor. When you have to explain it, it\'s bad.',
            'author': 'Cory House',
            'tags': ['programming', 'humor', 'code']
        }
    ]
    
    try:
        # Try multiple quote APIs
        apis = [
            'https://api.quotable.io/random',
            'https://quotes.rest/qod',  # Quote of the Day API
        ]
        
        for api_url in apis:
            try:
                response = requests.get(api_url, timeout=5, verify=False)  # Skip SSL verification for demo
                
                if response.status_code == 200:
                    quote_data = response.json()
                    
                    # Handle different API response formats
                    if 'content' in quote_data:  # Quotable API format
                        return Response({
                            'success': True,
                            'source': 'Quotable API',
                            'data': {
                                'quote': quote_data.get('content'),
                                'author': quote_data.get('author'),
                                'tags': quote_data.get('tags', []),
                            },
                            'message': 'Successfully fetched data from external API'
                        })
                    elif 'contents' in quote_data:  # Quote of the Day API format
                        quote = quote_data['contents']['quotes'][0]
                        return Response({
                            'success': True,
                            'source': 'Quote of the Day API',
                            'data': {
                                'quote': quote.get('quote'),
                                'author': quote.get('author'),
                                'tags': quote.get('tags', []),
                            },
                            'message': 'Successfully fetched data from external API'
                        })
            except:
                continue  # Try next API
        
        # If all APIs fail, use fallback quotes
        import random
        quote = random.choice(fallback_quotes)
        return Response({
            'success': True,
            'source': 'Fallback Quote Collection',
            'data': {
                'quote': quote['content'],
                'author': quote['author'],
                'tags': quote['tags'],
            },
            'message': 'Using local quote (external APIs unavailable)'
        })
            
    except Exception as e:
        # Final fallback
        import random
        quote = random.choice(fallback_quotes)
        return Response({
            'success': True,
            'source': 'Fallback Quote Collection',
            'data': {
                'quote': quote['content'],
                'author': quote['author'],
                'tags': quote['tags'],
            },
            'message': 'Using local quote due to error'
        })


@api_view(['GET'])
def weather_data(request):
    """
    Another third-party API integration example.
    Fetches weather data for a given city (optional).
    Uses wttr.in free weather API (no key required)
    """
    city = request.query_params.get('city', 'London')
    
    try:
        # Using wttr.in API which doesn't require API key
        response = requests.get(
            f'https://wttr.in/{city}?format=j1',
            timeout=5
        )
        
        if response.status_code == 200:
            weather_data = response.json()
            current = weather_data.get('current_condition', [{}])[0]
            
            return Response({
                'success': True,
                'source': 'wttr.in Weather API',
                'location': city,
                'data': {
                    'temperature': current.get('temp_C', 'N/A') + '°C',
                    'condition': current.get('weatherDesc', [{}])[0].get('value', 'N/A'),
                    'humidity': current.get('humidity', 'N/A') + '%',
                    'wind_speed': current.get('windspeedKmph', 'N/A') + ' km/h',
                    'feels_like': current.get('FeelsLikeC', 'N/A') + '°C',
                },
                'message': 'Successfully fetched weather data'
            })
        else:
            return Response({
                'success': False,
                'error': 'Failed to fetch weather data'
            }, status=status.HTTP_503_SERVICE_UNAVAILABLE)
            
    except requests.exceptions.RequestException as e:
        return Response({
            'success': False,
            'error': f'Weather API request failed: {str(e)}'
        }, status=status.HTTP_503_SERVICE_UNAVAILABLE)

