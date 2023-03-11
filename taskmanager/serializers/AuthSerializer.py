from django.contrib.auth.hashers import check_password
from django.db.models import ObjectDoesNotExist
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from taskmanager.models import User


class AuthSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        username = attrs['username']
        password = attrs['password']
        err = AuthenticationFailed("wrong credentials")
        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            raise err
        if not check_password(password, user.password):
            raise err
        tokens = self.get_token(user)
        data = {"refresh": str(tokens), "access": str(tokens.access_token)}
        return data

    @classmethod
    def get_token(cls, user):
        return cls.token_class.for_user(user)
