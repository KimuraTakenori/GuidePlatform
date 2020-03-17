
import datetime
from django.utils import timezone

from django import forms
from appGuide.models import *


class TouristReservationForm(forms.ModelForm):
    class Meta:
        model = Tourist
        fields = (
            "user_sei",
            "user_mei",
            "user_seifuri",
            "user_meifuri",
            "user_gender",
            "user_seinen",
            "user_tel",
            "user_mail",
            "user_pass",
            "user_post",
            "user_address1",
            "user_address2",
            "user_address3",
        )