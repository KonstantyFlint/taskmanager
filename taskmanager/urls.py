from django.contrib import admin
from django.urls import path

from taskmanager.views.UserView import UserView, CustomTokenObtainPairView
from taskmanager.views.TaskView import TaskListCreateView, TaskRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', TaskListCreateView.as_view()),
    path("tasks/<int:pk>", TaskRetrieveUpdateDestroyView.as_view()),
    path("users/", UserView.as_view()),
    path("token/", CustomTokenObtainPairView.as_view())
]
