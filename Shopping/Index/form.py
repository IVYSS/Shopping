from django.forms import ModelForm
from Index.models import Product
from django import forms
#################################

class ModelProduct(ModelForm):
    class Meta:
        model = Product
        fields = ['name','desc','stock','price','picture_url']



        labels = {
            'name': 'Name :',
            'desc' : 'Descriptions',
            'stock': 'Stock :',
            'price' : 'Price :',
            'picture_url' : 'Picture_url :',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'desc' : forms.Textarea(attrs={'class':'form-control'}),
            'stock' : forms.NumberInput (attrs={'class':'form-control'}),
            'price' : forms.NumberInput (attrs={'class':'form-control'}),
            'picture_url': forms.FileInput()  
            }