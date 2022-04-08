from django.urls import path
from images.views import ImageCreateView, ImageListView, ImageUpdateView

urlpatterns = [
    path("create/", ImageCreateView.as_view(), name="create_image"),
    path("mine/", ImageListView.as_view(), name="list_images"),
    path(
        "<int:pk>/complete/", ImageUpdateView.as_view(), name="complete_task"
    ),
]
