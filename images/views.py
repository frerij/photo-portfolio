from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from images.models import Image

# Create your views here.


class ImageCreateView(LoginRequiredMixin, CreateView):
    model = Image
    template_name = "images/create.html"
    fields = [
        "title",
        "date_taken",
        "img_link",
        "description",
        "collection",
        "photographer",
    ]

    def get_success_url(self) -> str:
        return reverse_lazy(
            "show_collection", args=[self.object.collection.id]
        )


class ImageListView(ListView):
    model = Image
    template_name = "images/list.html"

    def get_queryset(self):
        return Image.objects.filter(photographer=self.request.user)


class ImageUpdateView(LoginRequiredMixin, UpdateView):
    model = Image
    template_name = "images/edit.html"
    fields = [
        "title",
        "date_taken",
        "img_link",
        "description",
        "collection",
        "photographer",
    ]

    def get_success_url(self) -> str:
        return reverse_lazy(
            "show_collection", args=[self.object.collection.id]
        )
