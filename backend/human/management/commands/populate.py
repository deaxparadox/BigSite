from django.core.management.base import (
    BaseCommand, CommandError, CommandParser
)
import time 
import datetime
import typing
from typing import Optional, Any
import random
from faker import Faker
from faker.providers import BaseProvider

from info.models import Address
from human.models import (
    Human, SexChoices, MartialStatus, Alien
)
from extras.models.schools import School

class HumanProvider(BaseProvider):
    def age(self) -> int:
        return random.randint(10, 70)
    def phone(self) -> int:
        return random.randint(1000000000, 999999999)

class PopulateHuman(object):
    def __init__(self):
        self.__fake = Faker("en_IN")
        self.__fake.add_provider(HumanProvider)
        self.__name = None


    def generateUsername(self) -> str:
        """
        Return the generated username by first, middle, last name.
        """
        return "_".join(self.generateFirstMiddleLastName())
    
    def generateFirstMiddleLastName(self) -> typing.Tuple[str]:
        """
        Return the tuple of first, middle, last name
        """
        name = self.__fake.name().split(" ")
        match len(name):
            case 1:
                return name[0]
            case 2:
                first, last = name
                return first, last
            case _:
                first, middle, *last = name
                last = " ".join(last)
                return first, middle, last

    def generateAge(self) -> int:
        """
        Return age.
        """
        return self.__fake.age()
    
    
    def generateDateOfBirth(self) -> datetime.date:
        """
        Return date of birth.
        """
        leap = False 

        year = random.randint(1945, 2000)

        if year%4 == 0:
            leap = True 
         
        month = random.randint(1, 12)

        # day account to months
        if month == 2:
            if leap:
                day = random.randint(1, 29)
            else:    
                day = random.randint(1, 28)
        elif month in [4,6,9,11]:
            day = random.randint(1, 30)
        else:
            day = random.randint(1, 31)

            

        return datetime.date(
            year, month, day
        )
    
    def generateEmail(self) -> str:
        """
        Return email address.
        """
        return f"{self.generateUsername()}@email.com"

    def generatePhone(self) -> int:
        """
        Return phone
        """
        return random.randint(1000000000, 9999999999)
    
    def generateSex(self) -> str:
        """
        Return Sex.
        """
        return random.choice(
            [
                SexChoices.FEMALE.value, 
                SexChoices.MALE.value, 
                SexChoices.OTHER.value
            ]
        )
    def generateMartialStatus(self) -> str:
        """
        Return Martial Status.
        """
        return random.choice(
            [
                MartialStatus.UNMARRIED.value,
                MartialStatus.MARRIED.value
            ]
        )
    
    def generateAlien(self) -> int:
        """
        Return int.
        0: NO
        1: YES
        """
        return random.choice(
            [Alien.NO.value, Alien.YES.value]
        )
    
    def generateAddress(self) -> typing.Tuple[str]:
        """
        Return tuple of address
        """
        address = self.__fake.address().split(" ")
        match len(address):
            case 1:
                return address[0], "Uttar Pradesh", "india"
            case 2:
                street, city = address
                return street, city, "India"
            case _:
                street, city, *country = address
                if len(country) > 1:
                    country = " ".join(country)
                return street, city, country


    def generateSchool(self) -> typing.Tuple[str]:
        school_name = f"{' '.join(self.generateFirstMiddleLastName())} Public school"
        address = self.generateAddress()
        return school_name, Address.objects.create(
            street = address[0],
            city = address[1],
            country = address[2]
        )
    
            
                    
class Populate(PopulateHuman):
    def __init__(self):
        super().__init__()

    @property
    def username(self):
        """
        Return username
        """
        return self.generateUsername()
    @property
    def first_name(self) -> str:
        """
        Return first_name
        """
        self.__name = self.generateFirstMiddleLastName()
        return self.__name[0]

    @property
    def middle_name(self) -> str|None:
        """
        Return middle_name
        """
        return self.__name[1] if len(self.__name) > 2 else None
    
    def __last_name(self) -> str:
        return self.__name[len(self.__name)-1]

    @property
    def last_name(self) -> str:
        """
        Return last_name 
        """
        l_n = self.__last_name()
        return l_n

    @property
    def age(self):
        """
        Return age.
        """
        return self.generateAge()
    
    @property
    def date_of_birth(self):
        """
        Return date of birth
        """
        return self.generateDateOfBirth()
    
    @property
    def email(self):
        return self.generateEmail()
    
    @property
    def phone(self):
        return self.generatePhone()
    
    @property
    def sex(self):
        return self.generateSex()
    
    @property
    def married(self):
        return self.generateMartialStatus()
    
    @property
    def alien(self):
        return self.generateAlien()
    
    @property
    def address(self):
        address = self.generateAddress()
        return Address.objects.create(
            street = address[0],
            city = address[1],
            country = address[2]
        )
    
    @property
    def school(self):
        s = self.generateSchool()
        s_obj = School(
            name = s[0]
        )
        s_obj.save()
        s_obj.address.add(s[1])
        
        return s_obj


class Command(BaseCommand):
    help = "Populate the human models"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("--db", action="store_true")
        parser.add_argument("--entry", default=100, type=int)
        

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        for i in range(options.get("entry")):
            p = Populate()
            h = Human(
                username=p.username,
                first_name=p.first_name,
                middle_name=p.middle_name,
                last_name=p.last_name,
                age=p.age,
                date_of_birth=p.date_of_birth,
                phone=p.phone,
                email=p.email,
                sex=p.sex,
                married=p.married,
                alien=p.alien
            )

            h.save()

            h.address.add(p.address)
            h.school.add(p.school)

        self.stdout.write(self.style.SUCCESS(f"Successful"))