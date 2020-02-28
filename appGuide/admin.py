from django.contrib import admin

# Register your models here.

from .models import Gender, Tourist, Guide, Preplace, Place, Reservation,Guidetime, Guideplace

admin.site.register(Gender)
admin.site.register(Tourist)
admin.site.register(Guide)
admin.site.register(Preplace)
admin.site.register(Place)
admin.site.register(Reservation)
admin.site.register(Guidetime)
admin.site.register(Guideplace)
