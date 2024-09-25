from django.urls import reverse_lazy
from django.views import generic

from todo_list.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo_list/task_list.html"
    context_object_name = "tasks"


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = "todo_list/task_form.html"
    context_object_name = "form"
    fields = "__all__"
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = "todo_list/task_form.html"
    context_object_name = "form"
    fields = "__all__"
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo_list/delete_confirm.html"
    success_url = reverse_lazy("todo:task-list")


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo_list/tags_list.html"
    context_object_name = "tags"


class TagCreateView(generic.CreateView):
    model = Tag
    template_name = "todo_list/tag_form.html"
    context_object_name = "form"
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    template_name = "todo_list/tag_form.html"
    context_object_name = "form"
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todo_list/delete_confirm.html"
    success_url = reverse_lazy("todo:tag-list")
