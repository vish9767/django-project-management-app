from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets
router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet, basename='project')
router.register(r'tasks', views.TaskViewSet, basename='task')

urlpatterns = [
    # Router URLs for CRUD operations
    path('', include(router.urls)),
    
    # Custom endpoints
    path('dashboard/', views.dashboard_stats, name='dashboard-stats'),
    path('external/quotes/', views.fetch_external_data, name='external-quotes'),
    path('external/weather/', views.weather_data, name='weather-data'),
]
