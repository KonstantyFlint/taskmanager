from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer, Serializer

from taskmanager.models.User import User


class UserSerializer(ModelSerializer):
    password = CharField(style={'input_type': 'password'}, write_only=True)
    confirm_password = CharField(style={'input_type': 'password'}, write_only=True)

    def validate(self, attrs):
        confirm_password = attrs.pop('confirm_password')
        if attrs["password"] != confirm_password:
            raise ValidationError("the passwords are not matching")
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        if password:
            instance.set_password(password)
            instance.save()
        return super().update(instance, validated_data)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'password', 'confirm_password']


