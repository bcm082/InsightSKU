from django import forms
from .models import Product, Tag

class ClientNameForm(forms.Form):
    client_name = forms.CharField(label='Client Name', max_length=255)

class ProductForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Product
        fields = ['sku', 'asin', 'title', 'main_image', 'images_url', 'videos_url', 'a_plus_content_url', 'tags', 'notes', 'date_listed']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']