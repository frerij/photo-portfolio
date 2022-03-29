from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from projects.models import Project

# Create your views here.


class ProjectListView(LoginRequiredMixin, ListView):
    template_name = "projects/list.html"
    model = Project

    def get_queryset(self):
        return Project.objects.filter(members=self.request.user)


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "projects/detail.html"

    def get_queryset(self):
        return Project.objects.filter(members=self.request.user)


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = "projects/create.html"
    fields = [
        "name",
        "description",
        "members",
    ]

    def get_success_url(self, **kwargs):
        if kwargs is not None:
            return reverse_lazy("show_project", kwargs={"pk": self.object.pk})
        else:
            return reverse_lazy("show_project", args=(self.object.id))
