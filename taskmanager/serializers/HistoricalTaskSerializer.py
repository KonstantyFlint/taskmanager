from rest_framework.serializers import ModelSerializer

from taskmanager.models.Task import Task


class HistoricalTaskSerializer(ModelSerializer):
    class Meta:
        model = Task.history.model
        fields = ['id', 'history_id', 'name', 'description', 'status', 'user']


class ShortHistoricalTaskSerializer(ModelSerializer):
    class Meta:
        model = Task.history.model
        fields = ['history_id', 'id', 'name', 'status', 'user']
