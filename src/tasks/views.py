from django.shortcuts import render, redirect
from django.views.generic.base import View

from tasks.services import get_task_list, get_task_by_pk
from tasks.forms import TaskForm
from django.http import Http404

class TaskListView(View):
    def get(self, request, *args, **kwargs):
        task_list =get_task_list()
        context = {
            'task_list': task_list,
        }
        return render(request, 'tasks/task_list.html', context)

class TaskDetailView(View):
    def get(self, request, *args, **kwargs):
        task = get_task_by_pk(kwargs.get('pk'))
        context = {
            'task': task,
        }
        return render(request, 'tasks/task_detail.html', context)

class TaskCreateView(View):

    def get(self, request, *args, **kwargs):
        form = TaskForm()
        context = {
            'form': form,
        }
        return render(request, 'tasks/task_create.html', context)
    
    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task-list')
        else:
            raise Http404

class TaskUpdateView(View):
    
    def get(self, request, *args, **kwargs):
        task = get_task_by_pk(kwargs['pk'])
        form = TaskForm(instance=task)
        context = {
            'form': form,
        }
        return render(request, 'tasks/task_update.html', context)
    
    def post(self, request, *args, **kwargs):
        task = get_task_by_pk(kwargs['pk'])
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task-list')
        else:
            raise Http404


