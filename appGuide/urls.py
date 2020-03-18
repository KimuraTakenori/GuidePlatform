
from django.urls import path

from appGuide.views.search1 import GuidableTimeListView, search_guide
from appGuide.views.reserve1 import ReserveGuideTimeView

from appGuide.views.testviews import testview1, testview2, testview3

app_name = "appGuide"

urlpatterns = [
    path("search_guide",
         GuidableTimeListView.as_view(), name ="search_guide"),
    path("reserve_guide/<int:pk>",
         ReserveGuideTimeView.as_view(), name = "reserve_guide"),
    path("reserve_guide/<int:pk>/<str:cand_time_interval>", # ex. 202002031000_202002031130
         ReserveGuideTimeView.as_view(), name="reserve_guide"),


    path("testview1",
         testview1, name="testview1"),
    path("testview2",
         testview2, name="testview2"),
    path("testview3",
         testview3, name="testview3"),

    ]
