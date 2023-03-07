from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from taskmanager.models.Task import Task
from taskmanager.serializers.TaskSerializer import ShortTaskSerializer, TaskSerializer
from taskmanager.views.DefaultPagination import DefaultPagination


class ListCreateTaskView(ListCreateAPIView):
    queryset = Task.objects.all()
    filter_backends = []
    pagination_class = DefaultPagination
    permission_classes = []
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name', 'status', 'user']
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'status', 'user']


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
