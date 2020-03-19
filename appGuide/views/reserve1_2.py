
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

class ReserveGuideTimeView(TemplateView):

    template_name = "appGuide/reserve_guidetime1_2.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        guidable_time = GuidableTime.objects.get(pk = self.kwargs[ "pk" ])
        cdtimintvlstr = self.kwargs[ "cand_time_interval" ]

        req_time_from, req_time_to = [
            datetime_str_localize(tmpstr, "%Y%m%d%H%M")
            for tmpstr in cdtimintvlstr.split("_")
        ]

        if "reserve_form" not in vars(self):
            self.reserve_form = TouristReservationForm()
            self.reserve_form.fields[ "spot" ].queryset = guidable_time.guide.get_guidable_spots()

        context[ "guidable_time" ] = guidable_time
        context[ "req_time_from" ] = req_time_from
        context[ "req_time_to"   ] = req_time_to
        context[ "reserve_form" ]  = self.reserve_form

        if "no_longer_available" in vars(self):
            if self.no_longer_available:
                context[ "No_longer_avail" ] = True
            else:
                context[ "No_longer_avail" ] = False
        else:
            context[ "No_longer_avail" ] = None

        return context


    def post(self, request, *args, **kwargs):

        guidable_time = GuidableTime.objects.get(pk=self.kwargs[ "pk" ])
        cdtimintvlstr = self.kwargs[ "cand_time_interval" ]

        self.reserve_form = TouristReservationForm(data = self.request.POST)

        if self.reserve_form.is_valid():

            tourist       = self.reserve_form.save()
            spot          = self.reserve_form.cleaned_data[ "spot" ]

            req_time_from, req_time_to = [
                datetime_str_localize(tmpstr, "%Y%m%d%H%M")
                for tmpstr in cdtimintvlstr.split("_")
            ]

            # Check once more to confirm that the time interval is
            # still available, - not occupied by other tourist.

            if check_avail_full_interval(guidable_time,
                                         req_time_from, req_time_to):
                Reservation.objects.create(
                    tourist               = tourist,
                    reservation_ymdt      = timezone.localtime(),
                    reservation_time_from = req_time_from,
                    reservation_time_to   = req_time_to,
                    spot                  = spot,
                    guidable_time         = guidable_time,
                )
                return HttpResponseRedirect(reverse("appGuide:search_guide"))

            else:
                self.no_longer_available = True

        return self.get(request, *args, **kwargs)


