from django.urls import path
from .views import (
    TaskListView, 
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView
)

urlpatterns=[
    path('', TaskListView.as_view(), name='task-list'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('create/', TaskCreateView.as_view(), name='task-create'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
]