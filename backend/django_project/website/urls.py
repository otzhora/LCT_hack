from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('task/<task_name:task_name>/', views.task, name="task")
]