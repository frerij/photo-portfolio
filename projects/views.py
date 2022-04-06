from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from projects.models import Collection

# Create your views here.


class CollectionListView(LoginRequiredMixin, ListView):
    template_name = "projects/list.html"
    model = Collection

    def get_queryset(self):
        return Collection.objects.filter(members=self.request.user)


class CollectionDetailView(LoginRequiredMixin, DetailView):
    model = Collection
    template_name = "projects/detail.html"

    def get_queryset(self):
        return Collection.objects.filter(members=self.request.user)


class CollectionCreateView(LoginRequiredMixin, CreateView):
    model = Collection
    template_name = "projects/create.html"
    fields = [
        "title",
        "description",
    ]

    def get_success_url(self) -> str:
        return reverse_lazy("show_project", args=[self.object.id])
