from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import EventBasic,EventDetail,EventParticipant,EventTrainer
# Register your models here.

admin.site.register(EventBasic)
admin.site.register(EventDetail)
admin.site.register(EventParticipant)
admin.site.register(EventTrainer)