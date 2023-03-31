from django.contrib import admin

from .models import Address
from extras.models import india

@admin.register(Address)
class AddressModel(admin.ModelAdmin):
    pass 


@admin.register(india.State)
class StateAdmin(admin.ModelAdmin):
    pass


@admin.register(india.City)
class StateAdmin(admin.ModelAdmin):
    pass