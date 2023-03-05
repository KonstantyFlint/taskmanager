from rest_framework.generics import ListCreateAPIView

from taskmanager.models.User import User
from taskmanager.serializers.UserSerializer import UserSerializer
from taskmanager.views.DefaultPagination import DefaultPagination


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = DefaultPagination
    permission_classes = []

