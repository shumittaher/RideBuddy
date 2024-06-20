from .models import Locations
from django.forms import ModelForm


class LocationsForm(ModelForm):
    class Meta:
        model = Locations
        fields = '__all__' 
