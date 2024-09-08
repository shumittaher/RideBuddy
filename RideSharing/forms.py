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
            'trip_owner'
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
            'trip_owner': forms.HiddenInput()
        }

class BookingRequestCommentBox(forms.ModelForm):

    class Meta:

        model = Spot_Bookings
        fields = '__all__' 

        labels = {
            'requester_comments' : 'Additional Comments',
            'spots_requested' : 'Number of Spots'
        }

        widgets={
            'trip': forms.HiddenInput(),
            'requester': forms.HiddenInput(),
            'approval_status': forms.HiddenInput(),
           
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
        self.fields['spots_requested'] = forms.ChoiceField(
            choices=[(i, str(i)) for i in range(1, open_seats + 1)],
            widget=forms.Select(
                attrs={
                    "class": "form-control"
                }
            )
        )


        
class LocationSearchForm(forms.ModelForm):

    class Meta:
        model = Locations
        fields = ['location_area',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        location_areas = Locations.objects.order_by('location_area').values_list('location_area', flat=True).distinct()

        self.fields['location_area'] = forms.ChoiceField(label="Starting Area",
            choices=[('','All Locations')] + [(loc_area, loc_area) for loc_area in location_areas],
            widget=forms.Select(attrs={'class': 'form-control', 'id': 'location-area-searchbox'})
        )
        self.fields['destination_area'] = forms.ChoiceField(label="Destination Area",
            choices=[('','All Locations')] + [(loc_area, loc_area) for loc_area in location_areas],
            widget=forms.Select(attrs={'class': 'form-control', 'id': 'destination-area-searchbox'})
        )