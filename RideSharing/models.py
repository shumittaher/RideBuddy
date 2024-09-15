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
    trip_owner = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return f"Trip from {self.origin.location_name} to {self.destination.location_name}"

class Spot_Bookings(models.Model):

    trip = models.ForeignKey(Trips, on_delete=models.CASCADE)
    requester = models.ForeignKey(User, on_delete = models.CASCADE)
    spots_requested = models.PositiveSmallIntegerField()
    requester_comments = models.CharField(max_length=255)
    approval_status = models.BooleanField()

class Messages(models.Model):

    MESSAGE_TYPE_CHOICES = [
        ('approval', 'Approval'),
        ('rejection', 'Rejection'),
        ('request', 'Request'),
        ('info', 'Info'),
    ]

    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_recipient')
    content = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True)
    system_message = models.BooleanField(default=True)
    read = models.BooleanField(default=False)
    underlying_trip = models.ForeignKey(Trips, on_delete=models.CASCADE)
    underlying_booking = models.ForeignKey(Spot_Bookings, on_delete=models.SET_NULL, null=True, blank=True)
    message_type = models.CharField(max_length=10, choices=MESSAGE_TYPE_CHOICES)
    
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question



