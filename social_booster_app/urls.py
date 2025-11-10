"""
URL configuration for social_booster_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.shortcuts import render


def home_view(request):
    """Render the home page with API documentation"""
    return render(request, 'home.html')


def api_root_view(request):
    """JSON response for API root"""
    return JsonResponse({
        'message': 'Welcome to Social Booster Media API',
        'version': '1.0',
        'endpoints': {
            'admin': '/admin/',
            'api': '/api/',
            'projects': '/api/projects/',
            'tasks': '/api/tasks/',
            'dashboard': '/api/dashboard/',
            'external_quotes': '/api/external/quotes/',
            'weather': '/api/external/weather/',
        },
        'documentation': 'See README.md for full API documentation'
    })


urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

