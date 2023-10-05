from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic

from todo.forms import TaskForm
from todo.models import Task, Tag


def index(request):
    num_tags = Tag.objects.count()
    deadline_tasks = Task.objects.filter(deadline__isnull=False, is_done=False)[:5]
    num_tasks_done = Task.objects.filter(is_done=True).count()
    num_tasks_not_done = Task.objects.filter(is_done=False).count()
    context = {
        "num_tags": num_tags,
        "num_tasks_done": num_tasks_done,
        "num_tasks_not_done": num_tasks_not_done,
        "deadline_tasks": deadline_tasks,
    }
    return render(request, "todo/index.html", context)


class TaskDetailView(generic.DetailView):
    model = Task


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 10


class TaskCreateView(generic.CreateView):
    model = Task
    success_url = reverse_lazy("todo:task-list")
    form_class = TaskForm


class TaskUpdateView(generic.UpdateView):
    model = Task
    success_url = reverse_lazy("todo:task-list")
    form_class = TaskForm


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task-list")


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 15


class TagCreateView(generic.CreateView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
    form_class = TaskForm


class TagUpdateView(generic.UpdateView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
    fields = "__all__"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")


def mark_as_done(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_done = True
    task.save()
    return HttpResponseRedirect(reverse_lazy("todo:task-list"))
