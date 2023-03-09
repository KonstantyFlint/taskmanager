from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication

from taskmanager.models.Task import Task
from taskmanager.serializers.TaskSerializer import ShortTaskSerializer, TaskSerializer
from taskmanager.views.DefaultPagination import DefaultPagination
from taskmanager.views.OptionallyHistoricalView import OptionallyHistoricalView


class TaskListCreateView(OptionallyHistoricalView, ListCreateAPIView):
    pagination_class = DefaultPagination
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name', 'status', 'user']
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'status', 'user']
    queryset = Task.objects.all()
    historical_manager = Task.history

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ShortTaskSerializer
        else:
            return TaskSerializer


class TaskRetrieveUpdateDestroyView(OptionallyHistoricalView, RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    pagination_class = DefaultPagination
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    historical_manager = Task.history
