from django.urls import path

from . import views

urlpatterns = [
    path('get/', views.TodolistApi.as_view()),
    path('todo/<int:todo_id>/', views.TodoDetailApi.as_view()),
]