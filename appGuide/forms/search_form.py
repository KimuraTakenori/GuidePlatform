
import datetime
from django.utils import timezone

from django import forms
from appGuide.models import *

class SearchGuideForm(forms.Form):

    req_time_from = \
        forms.DateTimeField(
            # widget   = forms.DateTimeInput(
            # attrs    = { "type"  : "datetime-local",
            #              "value" : timezone.datetime.now().strftime('%Y-%m-%dT%H:%M')}),
            # input_formats=['%Y-%m-%dT%H:%M'],
            required = True,
            label    = "希望日時開始")

    req_time_to = \
        forms.DateTimeField(
            # widget   = forms.DateTimeInput(
            # attrs    = { "type"  : "datetime-local",
            #              "value" : timezone.datetime.now().strftime('%Y-%m-%dT%H:%M')}),
            # input_formats = [ '%Y-%m-%dT%H:%M' ],
            required = True,
            label    = "希望日時終了")

    place_choices = forms.ModelMultipleChoiceField(
        queryset = Spot.objects.all(),
        widget   = forms.CheckboxSelectMultiple(),
        label    = "希望観光場所",
        required = False)
