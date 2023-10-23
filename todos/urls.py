from django.urls import path

from todos import views

app_name = "todos"

urlpatterns = [
    path("todos/", views.TODOView.as_view(), name="todo-list"),
]
