from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView

from taskmanager.models.User import User
from taskmanager.serializers.UserSerializer import UserSerializer
from taskmanager.serializers.Auth import CustomTokenObtainPairSerializer
from taskmanager.views.DefaultPagination import DefaultPagination


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = DefaultPagination


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        refresh_token = response.data.get("refresh")
        access_token = response.data.get("access")
        if refresh_token and access_token:
            response.set_cookie(
                "refresh_token", refresh_token, httponly=True, samesite="strict"
            )
            response.set_cookie(
                "access_token", access_token, httponly=True, samesite="strict"
            )
        return response
