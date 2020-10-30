from django.urls import path

from . import views
from .views import ArticleView, TaskView

urlpatterns = [
    path('', ArticleView.as_view(), name='home'),
    path('task/<slug:url>/', TaskView.as_view(), name="task")
]