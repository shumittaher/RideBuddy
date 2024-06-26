from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    pass

class Locations(models.Model):
    LOCATION_TYPES = (
        ('school', 'School'),
        ('residential', 'Residential'),
    )

    location_area = models.CharField(max_length=200)
    location_name = models.CharField(max_length=200)
    embarcation_text = models.CharField(max_length=200)
    type = models.CharField(max_length=20, choices=LOCATION_TYPES)

    def __str__(self):
        return f"{self.location_area} - {self.location_name}"

    
class Trips(models.Model):
    origin = models.ForeignKey(Locations, on_delete = models.CASCADE, related_name = 'start_point')
    destination = models.ForeignKey(Locations, on_delete = models.CASCADE, related_name = 'end_point')
    description_text = models.TextField(null=True, blank=True)
    departure_time = models.TimeField()
    open_seats = models.IntegerField()
    valid_till = models.DateField()