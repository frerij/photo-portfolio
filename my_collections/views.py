from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from my_collections.models import Collection

# Create your views here.


class CollectionListView(ListView):
    template_name = "collections/list.html"
    model = Collection

    # def get_queryset(self):
    #     return Collection.objects.filter(photgrapher=self.request.user)


class CollectionDetailView(DetailView):
    model = Collection
    template_name = "collections/detail.html"

    # def get_queryset(self):
    #     return Collection.objects.filter(photographer=self.request.user)


class CollectionCreateView(LoginRequiredMixin, CreateView):
    model = Collection
    template_name = "collections/create.html"
    fields = [
        "title",
        "description",
        "cover_image",
    ]

    success_url = reverse_lazy("list_collections")
