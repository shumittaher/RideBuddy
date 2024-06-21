from .models import Trips
from django.forms import ModelForm


class TripsForm(ModelForm):
    class Meta:
        model = Trips
        fields = '__all__' 
