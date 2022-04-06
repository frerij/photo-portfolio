from django.urls import path
from tasks.views import ImageCreateView, ImageListView, ImageUpdateView

urlpatterns = [
    path("create/", ImageCreateView.as_view(), name="create_task"),
    path("mine/", ImageListView.as_view(), name="show_my_tasks"),
    path(
        "<int:pk>/complete/", ImageUpdateView.as_view(), name="complete_task"
    ),
]
