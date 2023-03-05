from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer, Serializer

from taskmanager.models.User import User


class UserSerializer(ModelSerializer):
    password = CharField(style={'input_type': 'password'}, write_only=True)
    confirm_password = CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'password', 'confirm_password']

    def validate(self, attrs):
        confirm_password = attrs.pop('confirm_password')
        if attrs["password"] != confirm_password:
            raise ValidationError("the passwords are not matching")
        return attrs
