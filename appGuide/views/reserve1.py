
from django.utils import timezone
from django.views.generic import TemplateView

from ..models import *
from ..forms.reserve_form import TouristReservationForm

from pprint import pprint

class ReserveGuideTimeView(TemplateView):

    template_name = "appGuide/reserve_guidetime1_1.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        guidable_time = GuidableTime.objects.get(pk = self.kwargs[ "pk" ])

        if "reserve_form" not in vars(self):
            self.reserve_form = TouristReservationForm()
            self.reserve_form.fields[ "spot" ].queryset = guidable_time.guide.get_guidable_spots()

        context[ "guidable_time" ] = guidable_time
        context[ "reserve_form" ]  = self.reserve_form

        return context


    def post(self, request, *args, **kwargs):

        self.reserve_form = TouristReservationForm(data = self.request.POST)

        if self.reserve_form.is_valid():
            tourist       = self.reserve_form.save()
            guidable_time = GuidableTime.objects.get(pk=self.kwargs["pk"])
            spot          = self.reserve_form.cleaned_data[ "spot" ]

            Reservation.objects.create(
                tourist               = tourist,
                reservation_ymdt      = timezone.localtime(),
                reservation_time_from = guidable_time.guidable_time_from,
                reservation_time_to   = guidable_time.guidable_time_to,
                spot                  = spot,
                guidable_time         = guidable_time,
            )

        return self.get(request, *args, **kwargs)
