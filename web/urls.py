from django.urls import path

from . import views

app_name = "web"

urlpatterns = [
    path("", views.home, name="home"),
    path("create_task/", views.create_task, name="create_task"),
    path("delete_task/<int:pk>", views.delete_task, name="delete_task"),
]
