from django.db import models

# Create your models here.

class Producto(models.Model):
    TipoProducto = models.CharField (max_length=50, help_text="the name of publisher.")
    Descripcion = models.CharField (max_length=50, help_text="the publisher description.")
    Talle = models.CharField (max_length=50, choices=[('S', 'S' ),('M','M'),('L','L'),('XL','XL'),('XXL','XXL')])
    Color = models.CharField (max_length=50, help_text="the publisher color.")
    Marca = models.CharField (max_length=50, help_text="the publisher marca.")
    PrecioCompra = models.FloatField ( help_text="the publisher precioCompra.")    
    PrecioVenta = models.FloatField ( help_text="the publisher PrecioVenta.")
    Stock = models.IntegerField ( help_text="the publisher stock.")
    
    def __str__(self) -> str:
        return self. Descripcion 

class Proveedor(models.Model):
    Nombre = models.CharField (max_length=50, help_text="the publisher description.")
    Telefono = models.IntegerField ( help_text="the publisher talle.")
    Localidad = models.CharField (max_length=50, help_text="the publisher talle.")
    Email = models.CharField (max_length=50, help_text="the publisher description.")

    def __str__(self) -> str:
        return self.Nombre
    
class Compra(models.Model):
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    Proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    Talle = models.CharField (max_length=50, choices=[('S', 'S' ),('M','M'),('L','L'),('XL','XL'),('XXL','XXL')])


class Vendedores(models.Model):
    Nombre = models.CharField (max_length=50, help_text="the publisher description.")
    Telefono = models.IntegerField (help_text="the publisher talle.")
    Direccion = models.CharField (max_length=50, help_text="the publisher talle.")

    def __str__(self) -> str:
        return self.Nombre

class Cliente(models.Model):
    Nombre = models.CharField (max_length=50, help_text="the publisher description.")
    Telefono = models.IntegerField (help_text="the publisher talle.")
    Direccion = models.CharField (max_length=50, help_text="the publisher talle.")
    Saldo = models.FloatField (help_text="the publisher precioCompra.") 

    def __str__(self) -> str:
        return self.Nombre

class Ventas(models.Model):
    Vendedor = models.ForeignKey(Vendedores, on_delete=models.CASCADE)
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    TipoVenta = models.CharField (max_length=50, help_text="the publisher description.")
    TipoPago = models.CharField (max_length=50, help_text="the publisher description.")
    Total = models.FloatField (help_text="the publisher talle.")
    Fecha = models.DateField (help_text="the publisher description.")

class VentaProd(models.Model):
    Ventas=  models.ForeignKey(Ventas, on_delete=models.CASCADE)
    Producto=  models.ForeignKey(Producto, on_delete=models.CASCADE)


   
    