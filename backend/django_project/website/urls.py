from django.urls import path

from . import views

from .views import ArticleView, TaskView, CodeView, NewTaskView, TasksView, ResultView


urlpatterns = [
    path('', ArticleView.as_view(), name='home'),
    path('task/<slug:url>/', TaskView.as_view(), name="task"),
    path('tasks/', TasksView.as_view(), name="tasks"),
    path('code/<slug:username>/<slug:url>/', CodeView.as_view(), name="code"),
    path('new_task', NewTaskView.as_view(), name="new_task"),
    path('results/<slug:username>/<slug:url>/', ResultView.as_view(), name="result"),
]
