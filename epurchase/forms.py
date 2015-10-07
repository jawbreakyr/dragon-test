from django.forms import ModelForm

from epurchase.models import Buyer, Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ['transaction']
