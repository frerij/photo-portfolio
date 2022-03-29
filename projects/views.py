from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from projects.models import Project

# Create your views here.


class ProjectListView(LoginRequiredMixin, ListView):
    template_name = "projects/list.html"
    model = Project

    def get_queryset(self):
        return Project.objects.filter(members=self.request.user)
