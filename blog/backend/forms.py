from socket import fromshare
from typing_extensions import Required
from django import forms

class BackendForm(forms.Form):
    name = forms.CharField(required=True)
    title = forms.CharField(required=True)
    content = forms.CharField(required=True)
    s = forms.IntegerField(required=True)
