
from django.urls import path

from appGuide.views.search1 import GuidableTimeListView, GuidableTimeIntervalView, search_guide
from appGuide.views.reserve1_2 import ReserveGuideTimeView

app_name = "appGuide"

urlpatterns = [

    path("search_guide",
         GuidableTimeIntervalView.as_view(), name ="search_guide"),
    path("reserve_guide/<int:pk>/<str:cand_time_interval>", # ex. 202002031000_202002031130
         ReserveGuideTimeView.as_view(), name="reserve_guide"),

    ]
