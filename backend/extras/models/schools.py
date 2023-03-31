from django.db import models 
import typing 

from info.models import Address

class School(models.Model):
    name = models.CharField(max_length=120)
    address = models.ManyToManyField(Address, related_name="school", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        app_label = 'human'

    def __str__(self):
        return self.name
    
    def get_cities(self) -> typing.List:
        return [x.city for x in self.address.all()]
    
    def in_city(self, city: str) -> bool:
        return True if city in self.get_cities() else False
    