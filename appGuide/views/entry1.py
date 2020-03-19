
# The following may be used for extracting portion of available time frames:
# pip install portion
# https://github.com/AlexandreDecan/portion

from datetime import datetime

from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView

from ..models import *
from ..forms.reserve_form import TouristReservationForm

from ..modules.datetime_with_timezone1 import datetime_str_localize
from ..modules.search_guidable_time_intervals1_1 import check_avail_full_interval

from pprint import pprint

class EntryView(TemplateView):

    template_name = "appGuide/entry1.html"



