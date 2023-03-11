from rest_framework.permissions import BasePermission


class TaskPermission(BasePermission):
    def has_object_permission(self, request, view, task_obj):
        return task_obj.user and request.user.id == task_obj.user.id
