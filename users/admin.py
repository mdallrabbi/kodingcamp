from django.contrib import admin

from .models import IndividualUser, OrganizationUser

admin.site.register(IndividualUser)
admin.site.register(OrganizationUser)
