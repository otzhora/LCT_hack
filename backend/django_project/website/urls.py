from django.urls import path

from . import views

from .views import ArticleView, TaskView, CodeView, NewTaskView, TasksView, ResultView, AssignView, ReviewView, \
    AssignedView, GetReviewView

urlpatterns = [
    path('', ArticleView.as_view(), name='home'),
    path('task/<slug:url>/', TaskView.as_view(), name="task"),
    path('tasks/', TasksView.as_view(), name="tasks"),
    path('code/<slug:username>/<slug:url>/', CodeView.as_view(), name="code"),
    path('new_task', NewTaskView.as_view(), name="new_task"),
    path('results/<slug:username>/<slug:url>/', ResultView.as_view(), name="result"),
    path('assign/', AssignView.as_view(), name="assign"),
    path('assigned/<slug:username>', AssignView.as_view(), name="assigned"),
    path('review', ReviewView.as_view(), name="review"),
    path('review/<slug:username>/<slug:url>', ReviewView.as_view(), name="review_get"),
    path('advanced', AdvancedView.as_view(), name="advanced"),
]
