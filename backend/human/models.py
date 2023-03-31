from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from info.models import Address
from extras.models.schools import School

class Time(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True 


class SexChoices(models.TextChoices):
    MALE = "M", _("Male")
    FEMALE = "F", _("Female")
    OTHER = "O", _("Other")

class MartialStatus(models.TextChoices):
    MARRIED = "M", _("Married")
    UNMARRIED = "U", _("Unmarried")

class Alien(models.IntegerChoices):
    NO = 0, _("No")
    YES = 1, _("Yes")

class Human(Time):
    username = models.CharField(max_length=120, primary_key=True, unique=True)
    picture = models.ImageField(blank=True, null=True, upload_to="human/%Y/%d/%m")
    first_name = models.CharField(max_length=30, blank=True, null=True)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    age = models.IntegerField()
    date_of_birth = models.DateField(blank=True, null=True)
    email = models.EmailField(max_length=120, blank=True, null=True)
    phone = models.PositiveBigIntegerField(unique=True, default=1234567890)
    sex = models.CharField(max_length=1, choices=SexChoices.choices)
    married = models.CharField(max_length=1, choices=MartialStatus.choices, default=MartialStatus.UNMARRIED)
    alien = models.IntegerField(default=Alien.NO, choices=Alien.choices)
    address = models.ManyToManyField(Address, related_name="human")
    school = models.ManyToManyField(School, related_name="human")


    def __str__(self) -> str:
        return self.username
    
    def underage(self) -> bool:
        """
        Return True if age < 18, else return False
        """
        return True if self.age < 18 else False
    
    @property
    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)
    
    def get_absolute_url(self):
        return reverse("human:detail", args=[self.username])
    
    class Meta:
        get_latest_by = "-created"
        ordering = ['username']
        verbose_name = "human"