from django.contrib import admin
from django.urls import path, include

from taskmanager.views.TaskChangesView import SingleTaskChangesView, AllTaskChangesView
from taskmanager.views.UserView import UserListCreateView, UserRetrieveUpdateDestroyView
from taskmanager.views.Auth import JWTLoginView, JWTLogoutView
from taskmanager.views.TaskView import TaskListCreateView, TaskRetrieveUpdateDestroyView

users = include([
    path("", UserListCreateView.as_view(), name="users"),
    path("<int:pk>", UserRetrieveUpdateDestroyView.as_view(), name="users-modify"),
    path("login/", JWTLoginView.as_view(), name="users-login"),
    path("logout/", JWTLogoutView.as_view(), name="users-logout"),
])

tasks = include([
    path('', TaskListCreateView.as_view(), name="all-tasks"),
    path("changes", AllTaskChangesView.as_view(), name="all-tasks-changes"),
    path("<int:pk>", TaskRetrieveUpdateDestroyView.as_view(), name="single-task"),
    path("<int:pk>/changes", SingleTaskChangesView.as_view(), name="single-task-changes"),
])

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', tasks),
    path("users/", users),
]
