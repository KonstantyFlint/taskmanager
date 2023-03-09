from rest_framework.permissions import IsAuthenticated


class IsAccountOwner(IsAuthenticated):
    def has_object_permission(self, request, view, user_obj):
        return request.user.id == user_obj.id
