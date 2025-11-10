from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from api.models import Project, Task
from decimal import Decimal


class Command(BaseCommand):
    help = 'Populates the database with sample data for demonstration'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating sample data...')
        
        # Clear existing data
        Project.objects.all().delete()
        Task.objects.all().delete()
        
        # Create sample projects
        projects_data = [
            {
                'title': 'E-commerce Website Redesign',
                'description': 'Complete redesign of the client\'s e-commerce platform with modern UI/UX and improved performance.',
                'client_name': 'TechMart Inc',
                'budget': Decimal('45000.00'),
                'status': 'in_progress',
                'start_date': timezone.now().date() - timedelta(days=15),
                'end_date': timezone.now().date() + timedelta(days=60),
            },
            {
                'title': 'Mobile App Development',
                'description': 'Native mobile application for iOS and Android with real-time synchronization.',
                'client_name': 'FitLife Solutions',
                'budget': Decimal('75000.00'),
                'status': 'planning',
                'start_date': timezone.now().date() + timedelta(days=7),
                'end_date': timezone.now().date() + timedelta(days=120),
            },
            {
                'title': 'Social Media Marketing Campaign',
                'description': 'Comprehensive social media marketing strategy with content creation and management.',
                'client_name': 'GreenLeaf Organics',
                'budget': Decimal('15000.00'),
                'status': 'completed',
                'start_date': timezone.now().date() - timedelta(days=90),
                'end_date': timezone.now().date() - timedelta(days=5),
            },
            {
                'title': 'Brand Identity Refresh',
                'description': 'Complete brand identity overhaul including logo, color scheme, and brand guidelines.',
                'client_name': 'Stellar Innovations',
                'budget': Decimal('28000.00'),
                'status': 'in_progress',
                'start_date': timezone.now().date() - timedelta(days=30),
                'end_date': timezone.now().date() + timedelta(days=15),
            },
            {
                'title': 'Data Analytics Dashboard',
                'description': 'Interactive dashboard for real-time business analytics and reporting.',
                'client_name': 'DataDrive Corp',
                'budget': Decimal('52000.00'),
                'status': 'planning',
                'start_date': timezone.now().date() + timedelta(days=14),
                'end_date': None,
            },
        ]
        
        created_projects = []
        for proj_data in projects_data:
            project = Project.objects.create(**proj_data)
            created_projects.append(project)
            self.stdout.write(f'  Created project: {project.title}')
        
        # Create tasks for each project
        tasks_data = [
            # Tasks for E-commerce Website
            {'project': created_projects[0], 'name': 'Design mockups', 'description': 'Create initial design mockups for all pages', 'priority': 'high', 'completed': True, 'due_date': timezone.now().date() - timedelta(days=10)},
            {'project': created_projects[0], 'name': 'Frontend development', 'description': 'Implement responsive frontend with React', 'priority': 'high', 'completed': False, 'due_date': timezone.now().date() + timedelta(days=20)},
            {'project': created_projects[0], 'name': 'Backend API setup', 'description': 'Set up REST API with Django', 'priority': 'high', 'completed': True, 'due_date': timezone.now().date() - timedelta(days=5)},
            {'project': created_projects[0], 'name': 'Database optimization', 'description': 'Optimize database queries and indexing', 'priority': 'medium', 'completed': False, 'due_date': timezone.now().date() + timedelta(days=30)},
            
            # Tasks for Mobile App
            {'project': created_projects[1], 'name': 'Requirements gathering', 'description': 'Document all functional requirements', 'priority': 'high', 'completed': False, 'due_date': timezone.now().date() + timedelta(days=5)},
            {'project': created_projects[1], 'name': 'UI/UX wireframes', 'description': 'Create wireframes for all app screens', 'priority': 'high', 'completed': False, 'due_date': timezone.now().date() + timedelta(days=10)},
            {'project': created_projects[1], 'name': 'API integration planning', 'description': 'Plan third-party API integrations', 'priority': 'medium', 'completed': False, 'due_date': timezone.now().date() + timedelta(days=15)},
            
            # Tasks for Social Media Campaign
            {'project': created_projects[2], 'name': 'Content strategy', 'description': 'Develop comprehensive content strategy', 'priority': 'high', 'completed': True, 'due_date': timezone.now().date() - timedelta(days=80)},
            {'project': created_projects[2], 'name': 'Content creation', 'description': 'Create posts, graphics, and videos', 'priority': 'high', 'completed': True, 'due_date': timezone.now().date() - timedelta(days=60)},
            {'project': created_projects[2], 'name': 'Campaign execution', 'description': 'Execute campaign across platforms', 'priority': 'high', 'completed': True, 'due_date': timezone.now().date() - timedelta(days=30)},
            {'project': created_projects[2], 'name': 'Analytics report', 'description': 'Prepare final analytics report', 'priority': 'medium', 'completed': True, 'due_date': timezone.now().date() - timedelta(days=7)},
            
            # Tasks for Brand Identity
            {'project': created_projects[3], 'name': 'Logo design', 'description': 'Design new logo variations', 'priority': 'high', 'completed': True, 'due_date': timezone.now().date() - timedelta(days=20)},
            {'project': created_projects[3], 'name': 'Color palette', 'description': 'Develop new color palette', 'priority': 'high', 'completed': True, 'due_date': timezone.now().date() - timedelta(days=15)},
            {'project': created_projects[3], 'name': 'Brand guidelines', 'description': 'Create comprehensive brand guidelines document', 'priority': 'medium', 'completed': False, 'due_date': timezone.now().date() + timedelta(days=10)},
            
            # Tasks for Data Analytics
            {'project': created_projects[4], 'name': 'Requirements analysis', 'description': 'Analyze client requirements and data sources', 'priority': 'high', 'completed': False, 'due_date': timezone.now().date() + timedelta(days=20)},
            {'project': created_projects[4], 'name': 'Dashboard design', 'description': 'Design dashboard layout and visualizations', 'priority': 'high', 'completed': False, 'due_date': timezone.now().date() + timedelta(days=35)},
            {'project': created_projects[4], 'name': 'Data pipeline setup', 'description': 'Set up automated data pipeline', 'priority': 'medium', 'completed': False, 'due_date': timezone.now().date() + timedelta(days=50)},
        ]
        
        for task_data in tasks_data:
            task = Task.objects.create(**task_data)
        
        self.stdout.write(f'  Created {len(tasks_data)} tasks')
        self.stdout.write(self.style.SUCCESS(f'\nSuccessfully created {len(created_projects)} projects and {len(tasks_data)} tasks'))
