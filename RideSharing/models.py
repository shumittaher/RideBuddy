from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    pass

from django.db import models

class Locations(models.Model):
    LOCATION_TYPES = (
        ('school', 'School'),
        ('residential', 'Residential'),
    )

    location_area = models.CharField(max_length=200)
    location_name = models.CharField(max_length=200)
    embarcation_text = models.CharField(max_length=200)
    type = models.CharField(max_length=20, choices=LOCATION_TYPES)

    
class Trips(models.Model):
    destination = models.ForeignKey(Locations, on_delete = models.CASCADE)