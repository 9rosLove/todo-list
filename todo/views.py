from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic

from todo.models import Task


def index(request):
    return render(request, "todo/index.html")


class TaskDetailView(generic.DetailView):
    model = Task


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task-list")


class TagListView(generic.ListView):
    model = Task


class TagCreateView(generic.CreateView):
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Task
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:tag-list")
