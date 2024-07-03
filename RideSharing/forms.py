from django import forms
from .models import Trips, Locations

class TripsForm(forms.ModelForm):

    VALID_FOR_CHOICES = [
        ('', 'Please Select'),
        ('monthly', 'Month'),
        ('quarterly', 'Quarter'),
        ('semi_annually', 'Half Year'),
        ('annually', 'Full Year'),
    ]


    valid_for = forms.ChoiceField(
        choices=VALID_FOR_CHOICES,
        widget=forms.Select(attrs={'class': "form-control", 'required': True}),
        label='Valid For'
    )

    class Meta:
        model = Trips
        fields = [
            'origin',
            'destination',
            'description_text',
            'departure_time',
            'open_seats',
            'valid_for',
            'valid_till',
        ]


        labels = {
            'origin': 'Starting Point',
            'destination': 'Destination',
            'description_text': 'Description',
            'departure_time': 'Start Time',
            'open_seats': 'Number of Open Seats',
            'valid_till': 'Valid Till',
        }

        widgets = {
            'origin': forms.Select(attrs={'class': "form-control", 'required': True}),
            'destination': forms.Select(attrs={'class': "form-control", 'required': True}),
            'description_text': forms.Textarea(attrs={'class': "form-control", 'rows': "7", 'required': False}),
            'departure_time': forms.TimeInput(attrs={'class': "form-control",'type': 'time'}),
            'open_seats': forms.NumberInput(attrs={'class': "form-control"}),
            'valid_till': forms.DateInput(attrs={'class': "form-control", 'type': 'date'}),
        }


class LocationSearchForm(forms.ModelForm):

    class Meta:
        model = Locations
        fields = ['location_area',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['location_area'] = forms.ChoiceField(
            choices=[('','All Locations')] + [(loc.id, loc.location_area) for loc in Locations.objects.all()],
            widget=forms.Select(attrs={'class': 'form-control', 'id': 'location-area-searchbox'})
        )