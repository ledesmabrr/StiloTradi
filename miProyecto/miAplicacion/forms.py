from django import forms
from .models import Vendedores, Cliente, Producto,Proveedor,Ventas,VentaProd,Compra,CompraProd 
class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ('Nombre','Telefono','Localidad','Email')
        widges = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'Localidad': forms.TextInput(attrs={'class': 'form-control'}), 
            'Email': forms.TextInput(attrs={'class': 'form-control'}),
        }


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
        fields = '__all__'
        widges = {
            'TipoProducto': forms.TextInput(attrs={'class': 'form-control'}),
            'Descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'Talle': forms.TextInput(attrs={'class': 'form-control'}),
            'Color': forms.TextInput(attrs={'class': 'form-control'}),
            'Marca': forms.TextInput(attrs={'class': 'form-control'}),
            'PrecioCompra': forms.NumberInput(attrs={'class': 'form-control', 'type': 'float'}),
            'PrecioVenta': forms.NumberInput(attrs={'class': 'form-control'}),
            'Stock': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class VentaProdForm(forms.ModelForm):
    class Meta:
        model = VentaProd
        fields = '__all__'
        widgets = {
            'Producto': forms.Select(attrs={'class': 'form-select'}),  
            'Ventas': forms.Select(attrs={'class': 'form-select'}), 
        }

class VentasForm(forms.ModelForm):
    class Meta:
        model = Ventas
        fields = '__all__'
        widgets = {
            'Vendedor':forms.Select(attrs={'class': 'form-select'}),
            'Cliente': forms.Select(attrs={'class': 'form-select'}),
            'TipoVenta': forms.TextInput(attrs={'class': 'form-control'}),
            'TipoPago': forms.TextInput(attrs={'class': 'form-control'}),
            'Total': forms.NumberInput(attrs={'class': 'form-control'}),
            'Fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    VentaProdFormset = forms.inlineformset_factory(Ventas,VentaProd,  form=VentaProdForm, extra=5)

    class TotalVenta(VentaProdFormset):
        def clean(self):
            super().clean()
            for form in self.forms:
                cantidad = form.cleaned_data.get("Cantidad")
                if cantidad is not None:
                    PrecioVenta = form.instance.TipoProducto.PrecioVenta
                    total = cantidad * PrecioVenta
                    form.instance.PrecioVenta = PrecioVenta
                    form.instance.Total = total


class CompraProdForm(forms.ModelForm):
    class Meta:
        model = CompraProd
        fields = '__all__'
        widgets = {
            'Compra': forms.Select(attrs={'class': 'form-select'}),
            'Producto': forms.Select(attrs={'class': 'form-select'}), 
        }
    

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = '__all__'
        widgets = {
            'Proveedor': forms.Select(attrs={'class': 'form-select'}),
            'Fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            
        }

    CompraProdFormset = forms.inlineformset_factory(Compra,CompraProd, form= CompraProdForm, extra=5)
