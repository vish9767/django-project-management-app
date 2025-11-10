from django.contrib import admin
from .models import Project, Task


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'client_name', 'status', 'budget', 'start_date', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['title', 'client_name', 'description']
    date_hierarchy = 'created_at'


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'project', 'priority', 'completed', 'due_date', 'created_at']
    list_filter = ['priority', 'completed', 'created_at']
    search_fields = ['name', 'description', 'project__title']
    date_hierarchy = 'created_at'

