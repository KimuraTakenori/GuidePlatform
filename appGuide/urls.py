
from django.urls import path

from .views import search_guide, testview1, testview2

app_name = "appGuide"

urlpatterns = [
    path("search_guide",
         search_guide, name = "search_guide"),
    path("testview1",
         testview1, name="testview1"),
    path("testview2",
         testview2, name="testview2"),

    ]
