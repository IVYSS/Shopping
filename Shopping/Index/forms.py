from django import forms
from django_countries.fields import CountryField
from django.forms import ModelForm
from .models import Address

class CheckoutFrom(ModelForm):
    class Meta:
        model = Address
        fields = "__all__"