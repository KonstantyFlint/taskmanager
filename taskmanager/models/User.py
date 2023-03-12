from django.contrib.auth.base_user import BaseUserManager

import django.db.models as md
from django.contrib.auth.models import AbstractUser


class UserManager(BaseUserManager):
    def create_user(self, **kwargs):
        password = kwargs.pop('password')
        user = self.model(**kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, **kwargs):
        password = kwargs.pop('password')
        user = self.model(**kwargs)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractUser):
    username = md.CharField(max_length=30, unique=True)
    first_name = md.CharField(max_length=50)
    last_name = md.CharField(max_length=50)

    USERNAME_FIELD = "username"

    objects = UserManager()

    class Meta:
        ordering = ['id']
