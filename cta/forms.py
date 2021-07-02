from django import forms
from .models import Form, Cuantovaser


class SdcForm(forms.ModelForm):
    address = forms.CharField(label='')
    nombre = forms.CharField(label='nombre')
    apellido = forms.CharField(label='apellido')
    edad = forms.CharField(label='edad')
    interpretacion = forms.CharField(label='interpretacion')
    urgente = forms.CharField(label='urgente')
    nombre_2 = forms.CharField(label='nombre_2')
    apellido_2 = forms.CharField(label='apellido_2')
    celular = forms.CharField(label='celular')
    class Meta:
        model = Cuantovaser
        fields = ['address', ]

