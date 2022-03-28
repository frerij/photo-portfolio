from django.shortcuts import render
from django.views.generic import ListView
from projects.models import Project

# Create your views here.


class ProjectListView(ListView):
    template_name = "projects/list.html"
    model = Project
