from django.shortcuts import render
from tasks.models import Task, TaskType
from django.views import generic


class TaskListView(generic.ListView):
    model = Task
    fields = "__all__"


class TaskDetailView(generic.DetailView):
    model = Task
    fields = "__all__"