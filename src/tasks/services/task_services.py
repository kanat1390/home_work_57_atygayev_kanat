from tasks.models import Task
from django.shortcuts import get_object_or_404

def get_task_list():
    return Task.objects.all()

def get_task_by_pk(pk):
    return get_object_or_404(Task, pk=pk)