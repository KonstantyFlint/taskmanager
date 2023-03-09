from django.contrib.auth.hashers import check_password
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from taskmanager.models import User


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        username = attrs['username']
        password = attrs['password']

        user = User.objects.get(username=username)

        if not check_password(password, user.password):
            raise AuthenticationFailed("wrong credentials")
        refresh = self.get_token(user)
        data = {"refresh": str(refresh), "access": str(refresh.access_token)}
        return data

    @classmethod
    def get_token(cls, user):
        return cls.token_class.for_user(user)