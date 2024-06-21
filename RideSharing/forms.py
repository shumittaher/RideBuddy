from .models import Trips
from django.forms import ModelForm


class TripsForm(ModelForm):
    class Meta:
        model = Trips

        fields = '__all__' 

        labels = {
            'origin': 'Starting Point',
            'destination': 'Destination',
            'description_text': 'Description',
            'departure_time': 'Start Time',
            'open_seats': 'Number of Open Seats',
            'valid_till': 'Valid Till',
        }