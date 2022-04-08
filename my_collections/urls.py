from django.views.generic import TemplateView
from django.urls import path
from my_collections.views import (
    CollectionListView,
    CollectionDetailView,
    CollectionCreateView,
)

urlpatterns = [
    path("", CollectionListView.as_view(), name="list_collections"),
    path("<int:pk>/", CollectionDetailView.as_view(), name="show_collection"),
    path("create/", CollectionCreateView.as_view(), name="create_collection"),
    path(
        "about/",
        TemplateView.as_view(template_name="collections/about.html"),
        name="about_page",
    ),
    path(
        "home/",
        TemplateView.as_view(template_name="collections/home.html"),
        name="home",
    ),
]
