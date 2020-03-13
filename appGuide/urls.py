
from django.urls import path

from .views import search_guide

app_name = "appGuide"

urlpatterns = [
    path("search_guide",
         search_guide, name = "search_guide"),

    ]
