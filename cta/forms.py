from django import forms
from .models import Cuantovaser


class SdcForm(forms.ModelForm):
    address = forms.CharField(label='')

    class Meta:
        model = Cuantovaser
        fields = ['address']

