from django.contrib import admin

# Register your models here.
from .models import Producto, Compra, Ventas, Proveedor, Vendedores, Cliente,VentaProd 

# Register your models here.
admin.site.register(Producto)
admin.site.register(Compra)
admin.site.register(VentaProd)
admin.site.register(Proveedor)
admin.site.register(Vendedores)
admin.site.register(Cliente)
admin.site.register(Ventas)
