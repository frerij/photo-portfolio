from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from tasks.models import Task

# Create your views here.


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/create.html"
    fields = [
        "name",
        "start_date",
        "due_date",
        "project",
        "assignee",
    ]

    def get_success_url(self) -> str:
        return reverse_lazy("show_project", args=[self.object.project.id])


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/list.html"

    def get_queryset(self):
        return Task.objects.filter(assignee=self.request.user)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "tasks/edit.html"
    fields = ["is_completed"]

    success_url = reverse_lazy("show_my_tasks")
