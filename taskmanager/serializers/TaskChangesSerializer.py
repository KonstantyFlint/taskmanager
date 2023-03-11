from rest_framework.serializers import ModelSerializer

from taskmanager.models.Task import Task


class TaskChangesSerializer(ModelSerializer):
    class Meta:
        model = Task.history.model
        fields = ['id', 'history_id', 'history_user', 'history_type', 'history_date', 'name', 'description', 'status', 'user']
        ordering = ['history_date']


class ShortHistoricalTaskSerializer(ModelSerializer):
    class Meta:
        model = Task.history.model
        fields = ['history_id', 'id', 'name', 'status', 'user']
