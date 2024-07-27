from django import forms
from .models import Trips, Locations, Spot_Bookings

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

class BookingRequestCommentBox(forms.ModelForm):

    class Meta:

        model = Spot_Bookings
        exclude = ['approval_status']

        labels = {
            'requester_comments' : 'Additional Comments',
            'spots_requested' : 'Number of Spots'
        }

        widgets={
            'trip': forms.HiddenInput(),
            'requester': forms.HiddenInput(),
            'spots_requested': forms.Select(
            attrs={
                    "class": "form-control"
            }
            ),
            'requester_comments' : forms.Textarea(
            attrs={
                    "class": "form-control", 
                    "rows": 3,
                    "maxlength": 255
                }
            )
        }

    def __init__(self, *args, **kwargs):
        open_seats = kwargs.pop('open_seats', 4)
        super().__init__(*args, **kwargs) 
        self.fields['spots_requested'].choices = [(i, str(i)) for i in range(1, open_seats + 1)]

        
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