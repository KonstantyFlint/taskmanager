from django.contrib import admin
from django.urls import path

from taskmanager.views.UserView import UserView
from taskmanager.views.TaskView import ListCreateTaskView, RetrieveUpdateDestroyTaskView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', ListCreateTaskView.as_view()),
    path("tasks/<int:pk>", RetrieveUpdateDestroyTaskView.as_view()),
    path("users/", UserView.as_view()),
]
