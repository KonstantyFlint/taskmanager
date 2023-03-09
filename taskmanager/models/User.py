from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

import django.db.models as md
from django.contrib.auth.models import PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, **kwargs):
        password = kwargs.pop('password')
        user = self.model(**kwargs)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = md.CharField(max_length=30, unique=True)
    first_name = md.CharField(max_length=50)
    last_name = md.CharField(max_length=50)
    is_staff = md.BooleanField(default=False)

    USERNAME_FIELD = "username"

    objects = UserManager()

    class Meta:
        ordering = ['id']