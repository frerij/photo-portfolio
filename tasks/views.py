from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from tasks.models import Image

# Create your views here.


class ImageCreateView(LoginRequiredMixin, CreateView):
    model = Image
    template_name = "tasks/create.html"
    fields = [
        "title",
        "date_taken",
        "img_link",
        "description",
        "collection",
        "photographer",
    ]

    def get_success_url(self) -> str:
        return reverse_lazy("show_project", args=[self.object.project.id])


class ImageListView(LoginRequiredMixin, ListView):
    model = Image
    template_name = "tasks/list.html"

    def get_queryset(self):
        return Image.objects.filter(assignee=self.request.user)


class ImageUpdateView(LoginRequiredMixin, UpdateView):
    model = Image
    template_name = "tasks/edit.html"
    fields = ["is_completed"]

    success_url = reverse_lazy("show_my_tasks")
