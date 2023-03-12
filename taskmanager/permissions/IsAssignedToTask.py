from rest_framework.permissions import IsAuthenticated


class IsAssignedToTask(IsAuthenticated):
    message = "you cannot modify tasks you are not assigned to"

    def has_object_permission(self, request, view, task_obj):
        return task_obj.user and request.user.id == task_obj.user.id
