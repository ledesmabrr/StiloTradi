from django import forms
from .models import Vendedores, Cliente, Producto

class VendedoresForm(forms.ModelForm):
    class Meta:
        model = Vendedores
        fields = ('Nombre','Telefono','Direccion')
        widges = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'Direccion': forms.TextInput(attrs={'class': 'form-control'}),
        }
        

class ClientesForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('Nombre','Telefono','Direccion','Saldo')
        widges = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'Direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'Saldo': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('TipoProducto','Descripcion','Talle','Color','Marca','PrecioCompra','PrecioVenta','Stock')
        widges = {
            'TipoProducto': forms.TextInput(attrs={'class': 'form-control'}),
            'Descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'Talle': forms.TextInput(attrs={'class': 'form-control'}),
            'Color': forms.TextInput(attrs={'class': 'form-control'}),
            'Marca': forms.TextInput(attrs={'class': 'form-control'}),
            'PrecioCompra': forms.NumberInput(attrs={'class': 'form-control'}),
            'PrecioVenta': forms.NumberInput(attrs={'class': 'form-control'}),
            'Stock': forms.NumberInput(attrs={'class': 'form-control'}),
        }