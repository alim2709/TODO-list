from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from catalog.forms import TaskForm
from catalog.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "catalog/index.html"
    queryset = Task.objects.all().prefetch_related("tags__tasks")

    def post(self, request, *args, **kwargs):
        task = Task.objects.get(pk=request.POST.get("task_id"))
        if task.is_completed:
            task.is_completed = False
        else:
            task.is_completed = True
        task.save()
        return redirect("catalog:todo-list")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "catalog/task-form.html"
    success_url = reverse_lazy("catalog:todo-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "catalog/task-form.html"
    success_url = reverse_lazy("catalog:todo-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    fields = "__all__"
    template_name = "catalog/task_confirm_delete.html"
    success_url = reverse_lazy("catalog:todo-list")





class TagListView(generic.ListView):
    model = Tag
    template_name = "catalog/tag_list.html"
    queryset = Tag.objects.all()


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    template_name = "catalog/tag-form.html"
    success_url = reverse_lazy("catalog:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "catalog/tag-form.html"
    success_url = reverse_lazy("catalog:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    fields = "__all__"
    template_name = "catalog/tag_confirm_delete.html"
    success_url = reverse_lazy("catalog:tag-list")



