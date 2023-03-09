from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_filters.backends import DjangoFilterBackend
from rest_framework_simplejwt.authentication import JWTAuthentication

from taskmanager.models import Task
from taskmanager.serializers.TaskChangeSerializer import HistoricalTaskSerializer
from taskmanager.views.DefaultPagination import DefaultPagination


class SingleTaskChangesView(ListAPIView):
    pagination_class = DefaultPagination
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name', 'status', 'user']
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'status', 'user']
    queryset = Task.history
    serializer_class = HistoricalTaskSerializer

    def filter_queryset(self, queryset):
        task_id = self.kwargs["pk"]
        queryset = queryset.filter(id=task_id)
        return queryset


class AllTaskChangesView(ListAPIView):
    pagination_class = DefaultPagination
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name', 'status', 'user']
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'status', 'user']
    queryset = Task.history
    serializer_class = HistoricalTaskSerializer
