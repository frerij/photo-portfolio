from django.urls import path
from projects.views import (
    CollectionListView,
    CollectionDetailView,
    CollectionCreateView,
)

urlpatterns = [
    path("", CollectionListView.as_view(), name="list_projects"),
    path("<int:pk>/", CollectionDetailView.as_view(), name="show_project"),
    path("create/", CollectionCreateView.as_view(), name="create_project"),
]
