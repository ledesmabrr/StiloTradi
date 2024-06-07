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
<<<<<<< HEAD
            'Stock': forms.NumberInput(attrs={'class': 'form-control',  'min': '0'}),
        }


#class VentaProdForm(forms.ModelForm):
#    class Meta:
#        model = VentaProd
#        fields = '__all__'
#        widgets = {
#            'Producto': forms.Select(attrs={'class': 'form-select'}),  
#            'Ventas': forms.Select(attrs={'class': 'form-select'}), 
#        }
=======
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
>>>>>>> ef46de54e7253ec7cb346e267ecb0e25ae032dca

class VentasForm(forms.ModelForm):
    class Meta:
        model = Ventas
        fields = '__all__'
        widgets = {
            'Vendedor':forms.Select(attrs={'class': 'form-select'}),
            'Cliente': forms.Select(attrs={'class': 'form-select'}),
            'TipoVenta': forms.TextInput(attrs={'class': 'form-control'}),
            'TipoPago': forms.TextInput(attrs={'class': 'form-control'}),
<<<<<<< HEAD
            'Fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), 
            'Total': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'})
        }

class VentaProdForm(forms.ModelForm):
    PrecioVenta = forms.FloatField(label='Precio de Venta', required=False, widget=forms.TextInput(attrs={'readonly': True}))
    Total = forms.FloatField(label='Total', required=False)
    SubTotal = forms.FloatField(label='SubTotal', required=False, widget=forms.TextInput(attrs={'readonly': True}))
    

    class Meta:
        model = VentaProd
        fields = ['Ventas','Producto', 'Cantidad', 'PrecioVenta', 'SubTotal']
        widgets = {
            'Ventas': forms.Select(attrs={'class': 'form-select'}),
            'Producto': forms.Select(attrs={'class': 'form-select', 'onchange': 'updatePriceAndTotal(this)'}),
            'Cantidad': forms.NumberInput(attrs={'class': 'form-control', 'oninput': 'updateTotal(this)',  'min': '0'}),
            'PrecioVenta': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'SubTotal': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True})
        }
    
    def clean(self):
        cleaned_data = super().clean()
        cantidad = cleaned_data.get("Cantidad")
        precio_venta = cleaned_data.get("precio_venta")
        if cantidad is not None and precio_venta is not None:
            cleaned_data['SubTotal'] = cantidad * precio_venta
            
            # Calcular el total
            venta_prod_formset = self.instance.ventas_venta_prod.all()
            total = sum(form.cleaned_data.get('SubTotal', 0) for form in venta_prod_formset)
            self.instance.Total = total
        return cleaned_data
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        producto = instance.Producto
        if instance.Cantidad and producto.PrecioVenta:  # Corrección aquí
            instance.SubTotal = instance.Cantidad * producto.PrecioVenta  # Corrección aquí
        if commit:
            instance.save()
        return instance
        
    def __init__(self, *args, **kwargs):
        precio_venta = kwargs.pop('precio_venta', None)
        super().__init__(*args, **kwargs)
        self.fields['Producto'].required = False
        self.fields['SubTotal'].required = False
        if precio_venta is not None:
            self.fields['precio_venta'].initial = precio_venta

class BaseVentaProdFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()
        for form in self.forms:
            if not form.cleaned_data.get('DELETE', False):
                if 'Producto' in form.cleaned_data:
                    if not form.cleaned_data.get('Producto'):
                        form.add_error('Producto', 'Este campo es requerido')


# Definición del formset utilizando el formulario VentaProdForm
VentaProdFormset = forms.inlineformset_factory(
    Ventas, VentaProd, form=VentaProdForm, formset=BaseVentaProdFormSet, extra=5, can_delete=True
)

=======
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
    
>>>>>>> ef46de54e7253ec7cb346e267ecb0e25ae032dca

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = '__all__'
        widgets = {
            'Proveedor': forms.Select(attrs={'class': 'form-select'}),
            'Fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
<<<<<<< HEAD
            'Total': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'})
            
        }


class CompraProdForm(forms.ModelForm):
    PrecioCompra = forms.FloatField(label='Precio de Compra', required=False, widget=forms.TextInput(attrs={'readonly': True}))
    Total = forms.FloatField(label='Total', required=False)
    SubTotal = forms.FloatField(label='SubTotal', required=False, widget=forms.TextInput(attrs={'readonly': True}))

    class Meta:
        model = CompraProd
        fields = 'Compra','Producto', 'Cantidad', 'PrecioCompra', 'SubTotal'
        widgets = {
            'Compra': forms.Select(attrs={'class': 'form-select'}),
            'Producto': forms.Select(attrs={'class': 'form-select', 'onchange': 'updatePriceAndTotal(this)'}),
            'Cantidad': forms.NumberInput(attrs={'class': 'form-control', 'oninput': 'updateTotal(this)',  'min': '0'}),
            'PrecioCompra': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'SubTotal': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'})
        }

    def clean(self):
        cleaned_data = super().clean()
        cantidad = cleaned_data.get("Cantidad")
        precio_compra = cleaned_data.get("precio_compra")
        if cantidad is not None and precio_compra is not None:
            cleaned_data['SubTotal'] = cantidad * precio_compra
            
            # Calcular el total
            compra_prod_formset = self.instance.ventas_venta_prod.all()
            total = sum(form.cleaned_data.get('SubTotal', 0) for form in compra_prod_formset)
            self.instance.Total = total
        return cleaned_data
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        producto = instance.Producto
        if instance.Cantidad and producto.PrecioCompra:  # Corrección aquí
            instance.SubTotal = instance.Cantidad * producto.PrecioCompra  # Corrección aquí
        if commit:
            instance.save()
        return instance
    
    def __init__(self, *args, **kwargs):
        precio_compra = kwargs.pop('precio_compra', None)
        super().__init__(*args, **kwargs)
        self.fields['Producto'].required = False
        self.fields['SubTotal'].required = False
        if precio_compra is not None:
            self.fields['precio_compra'].initial = precio_compra
    

class BaseCompraProdFormset(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()
        for form in self.forms:
            if not form.cleaned_data.get('DELETE', False):
                if 'Producto' in form.cleaned_data:
                    if not form.cleaned_data.get('Producto'):
                        form.add_error('Producto', 'Este campo es requerido')


# Definición del formset utilizando el formulario VentaProdForm
CompraProdFormset = forms.inlineformset_factory(
    Compra, CompraProd, form=CompraProdForm, formset=BaseCompraProdFormset, extra=5, can_delete=True
)
=======
            
        }

    CompraProdFormset = forms.inlineformset_factory(Compra,CompraProd, form= CompraProdForm, extra=5)
>>>>>>> ef46de54e7253ec7cb346e267ecb0e25ae032dca
