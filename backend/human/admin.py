from django.contrib import admin

from .models import Human
from extras.models import schools

@admin.register(Human)
class HumanAdmin(admin.ModelAdmin):
    exclude = ("created", "updated")

@admin.register(schools.School)
class SchoolAdmin(admin.ModelAdmin):
    pass 