from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from tasks.services import get_task_list


class TaskListView(View):
    def get(self, request, *args, **kwargs):
        task_list =get_task_list()
        context = {
            'task_list': task_list,
        }
        return render(request, 'tasks/task_list.html', context)

