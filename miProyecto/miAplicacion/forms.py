from django import forms
from .models import Vendedores

class VendedoresForm(forms.ModelForm):
    class Meta:
        model = Vendedores
        fields = ('Nombre','Telefono','Direccion')
        widges = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'Direccion': forms.TextInput(attrs={'class': 'form-control'}),
        }
        #help_text = {
        #   'Nombre': '',
        #    'Telefono': '',
        #   'Direccion':'',
        #}