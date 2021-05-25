from django.urls import path, include

from . import views

app_name = "web"

urlpatterns = [
    path("", views.home, name="home"),
    path("crear_tarea/", views.crear_tarea, name="crear_tarea"),
    path("borrar_tarea/<int:pk>", views.borrar_tarea, name="borrar_tarea"),
]
