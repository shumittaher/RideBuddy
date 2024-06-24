from .models import Trips
from django import forms

class TripsForm(forms.ModelForm):
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

        widgets = {
            'origin': forms.Select(attrs={'class':"form-control", 'required': True}),
            'destination': forms.Select(attrs={'class':"form-control", 'required': True}),
            'description_text': forms.Textarea(attrs={'class':"form-control", 'rows': "7"}),
            'departure_time': forms.TimeInput(attrs={'class':"form-control",}),
            'open_seats': forms.NumberInput(attrs={'class':"form-control"}),
            'valid_till': forms.DateInput(attrs={'class':"form-control"}),
        }