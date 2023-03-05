from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from taskmanager.models.Task import Task
from taskmanager.serializers.TaskSerializer import ShortTaskSerializer, TaskSerializer
from taskmanager.views.DefaultPagination import DefaultPagination


class ListCreateTaskView(ListCreateAPIView):
    queryset = Task.objects.all()
    pagination_class = DefaultPagination
    permission_classes = []

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ShortTaskSerializer
        else:
            return TaskSerializer


class RetrieveUpdateDestroyTaskView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    pagination_class = DefaultPagination
    permission_classes = []
    serializer_class = TaskSerializer

