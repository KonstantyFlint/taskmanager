from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
import django.db.models as md


class UserManager(BaseUserManager):
    def create_user(self, **kwargs):
        password = kwargs.pop('password')
        kwargs["is_superuser"] = False
        kwargs["is_staff"] = False
        user = self.model(**kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, **kwargs):
        password = kwargs.pop('password')
        kwargs["is_superuser"] = True
        kwargs["is_staff"] = True
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
