
from django.views.generic import TemplateView

from ..models import GuidableTime
from ..forms.reserve_form import TouristReservationForm

from pprint import pprint

class ReserveGuideTimeView(TemplateView):

    template_name = "appGuide/reserve_guidetime1_1.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        guidable_time = GuidableTime.objects.get(pk = self.kwargs[ "pk" ])

        reserve_form = TouristReservationForm()

        context[ "guidable_time" ] = guidable_time
        context[ "reserve_form" ]  = reserve_form

        return context

