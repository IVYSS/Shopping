from django.forms import ModelForm
from Index.models import Product
#################################

class ModelProduct(ModelForm):
    class Meta:
        model = Product
        fields = ['name','desc','stock','price','picture_url']