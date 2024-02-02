from django import forms
from .models import Product

class ClientNameForm(forms.Form):
    client_name = forms.CharField(label='Client Name', max_length=255)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['client']

