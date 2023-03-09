from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser

from taskmanager.models.User import User
from taskmanager.permissions.IsAccountOwner import IsAccountOwner
from taskmanager.permissions.ReadOnly import ReadOnly
from taskmanager.serializers.UserSerializer import UserSerializer
from taskmanager.views.DefaultPagination import DefaultPagination


class UserListCreateView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = DefaultPagination
    permission_classes = [AllowAny]


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser | IsAccountOwner | ReadOnly]
