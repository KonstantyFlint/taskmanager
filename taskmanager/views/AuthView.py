from django.urls import reverse_lazy
from django.views.generic import RedirectView
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from taskmanager.serializers.AuthSerializer import AuthSerializer


class UserLoginView(TokenObtainPairView):
    serializer_class = AuthSerializer

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


class UserLogoutView(RedirectView):
    url = reverse_lazy('users')

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        response.message = "Logged out successfully"
        user = self.request.user
        if user and user.is_authenticated:
            blacklisted = BlacklistedToken(token=str(user.outstanding_token))
            blacklisted.save()
        response.delete_cookie("refresh_token")
        response.delete_cookie("access_token")
        return response
