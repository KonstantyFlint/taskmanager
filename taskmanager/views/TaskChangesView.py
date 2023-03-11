from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.authentication import JWTAuthentication

from taskmanager.models import Task
from taskmanager.serializers.TaskChangesSerializer import TaskChangesSerializer
from taskmanager.views.DefaultPagination import DefaultPagination


class SingleTaskChangesView(ListAPIView):
    """
    list of changes of one task
    """
    pagination_class = DefaultPagination
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'name', 'status', 'user', 'description', 'history_type', 'history_user', 'history_date']
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'history_date']
    queryset = Task.history
    serializer_class = TaskChangesSerializer

    def filter_queryset(self, queryset):
        task_id = self.kwargs["pk"]
        queryset = queryset.filter(id=task_id)
        return queryset


class AllTaskChangesView(ListAPIView):
    """
    list of changes of all tasks
    """
    pagination_class = DefaultPagination
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'name', 'status', 'user', 'history_type', 'history_user', 'history_type', 'history_date']
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'history_date']
    queryset = Task.history
    serializer_class = TaskChangesSerializer
