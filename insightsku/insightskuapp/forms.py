from django import forms

class ClientNameForm(forms.Form):
    client_name = forms.CharField(label='Client Name', max_length=255)
