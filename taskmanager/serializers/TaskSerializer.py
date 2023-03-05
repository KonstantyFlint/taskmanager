from rest_framework.serializers import ModelSerializer

from taskmanager.models.Task import Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'status', 'user']


class ShortTaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['name', 'status', 'user']
