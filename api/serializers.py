from rest_framework import serializers
from .models import Project, Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for Task model"""
    
    class Meta:
        model = Task
        fields = [
            'id', 'project', 'name', 'description', 
            'priority', 'completed', 'due_date', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer for Project model with nested tasks"""
    tasks = TaskSerializer(many=True, read_only=True)
    total_tasks = serializers.SerializerMethodField()
    completed_tasks = serializers.SerializerMethodField()
    
    class Meta:
        model = Project
        fields = [
            'id', 'title', 'description', 'client_name', 'budget',
            'status', 'start_date', 'end_date', 'created_at', 
            'updated_at', 'tasks', 'total_tasks', 'completed_tasks'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_total_tasks(self, obj):
        """Returns total number of tasks for this project"""
        return obj.tasks.count()
    
    def get_completed_tasks(self, obj):
        """Returns number of completed tasks for this project"""
        return obj.tasks.filter(completed=True).count()


class ProjectListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for listing projects"""
    total_tasks = serializers.SerializerMethodField()
    
    class Meta:
        model = Project
        fields = [
            'id', 'title', 'client_name', 'budget', 
            'status', 'start_date', 'total_tasks', 'created_at'
        ]
    
    def get_total_tasks(self, obj):
        return obj.tasks.count()
