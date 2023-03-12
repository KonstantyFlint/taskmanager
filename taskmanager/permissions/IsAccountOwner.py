from rest_framework.permissions import IsAuthenticated


class IsAccountOwner(IsAuthenticated):
    message = "you can only modify your own user detail"

    def has_object_permission(self, request, view, user_obj):
        return request.user.id == user_obj.id
