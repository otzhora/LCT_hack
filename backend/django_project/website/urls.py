from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('task/<slug:task_name>/', views.task, name="task")
]