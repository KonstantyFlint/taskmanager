from django.urls import path, include

from taskmanager.views.TaskChangesView import SingleTaskChangesView, AllTaskChangesView
from taskmanager.views.UserView import UserListView, UserRetrieveUpdateDestroyView, UserRegisterView
from taskmanager.views.AuthView import UserLoginView, UserLogoutView
from taskmanager.views.TaskView import TaskListCreateView, TaskRetrieveUpdateDestroyView

users = include([
    path("", UserListView.as_view(), name="users"),
    path("<int:pk>", UserRetrieveUpdateDestroyView.as_view(), name="users-modify"),
    path("register/", UserRegisterView.as_view(), name="users-logout"),
    path("login/", UserLoginView.as_view(), name="users-login"),
    path("logout/", UserLogoutView.as_view(), name="users-logout"),
])

tasks = include([
    path('', TaskListCreateView.as_view(), name="all-tasks"),
    path("changes", AllTaskChangesView.as_view(), name="all-tasks-changes"),
    path("<int:pk>", TaskRetrieveUpdateDestroyView.as_view(), name="single-task"),
    path("<int:pk>/changes", SingleTaskChangesView.as_view(), name="single-task-changes"),
])

urlpatterns = [
    path('tasks/', tasks),
    path("users/", users),
]
