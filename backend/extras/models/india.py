from django.db import models

from .others import TimeIt

class State(TimeIt):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, blank=True, null=True)
    
    class Meta:
        app_label = "info"
        ordering = ["name"]
        get_latest_by = ['-created']

class City(TimeIt):
    name = models.CharField(max_length=120)
    state = models.ForeignKey(State, related_name="city", on_delete=models.CASCADE)
    slug = models.SlugField(max_length=120, blank=True, null=True)

    class Meta:
        app_label = "info"
        ordering = ["name"]
        get_latest_by = ['-created']
