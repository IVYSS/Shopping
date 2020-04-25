from django import forms
from django_countries.fields import CountryField
from django.forms import ModelForm
from .models import Address
from django_countries.widgets import CountrySelectWidget

class CheckoutFrom(ModelForm):
    class Meta:
        model = Address
        exclude = ['user']
        widgets = {
            'payment_option': forms.RadioSelect,
            'street_address' : forms.TextInput(attrs={
                'placeholder': "1234 Main St",
                'class': 'mt-3',
            }),
            'apartment_address' :forms.TextInput(attrs={
                'placeholder': "Apartment or suite",
                'class': 'mt-3',
            }),
            'country' :CountrySelectWidget(attrs={
                'class': 'custom-select d-block w-100'}),
                
        }