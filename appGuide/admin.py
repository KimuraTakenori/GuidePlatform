from django.contrib import admin

# Register your models here.

from .models import Tourist, Guide, Gender

admin.site.register(Tourist)
admin.site.register(Guide)
admin.site.register(Gender)
