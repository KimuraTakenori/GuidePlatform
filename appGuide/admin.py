from django.contrib import admin

# Register your models here.

from .models import Gender, Tourist, Guide, PreTourSpot, Spot, Reservation,GuidableTime, GuidableSpot

admin.site.register(Gender)
admin.site.register(Tourist)
admin.site.register(Guide)
admin.site.register(PreTourSpot)
admin.site.register(Spot)
admin.site.register(Reservation)
admin.site.register(GuidableTime)
admin.site.register(GuidableSpot)
