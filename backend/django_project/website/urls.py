from django.urls import path

from . import views
from .views import ArticleView

urlpatterns = [
    path('', ArticleView.as_view(), name='home'),
    path('task/<slug:task_name>/', views.task, name="task")
]