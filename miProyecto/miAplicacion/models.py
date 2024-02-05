from django.db import models
# Create your models here.

    
class Producto(models.Model):
    TipoProducto = models.CharField (max_length=50)
    Descripcion = models.CharField (max_length=50)
    Talle = models.CharField (max_length=50, choices=[('S', 'S' ),('M','M'),('L','L'),('XL','XL'),('XXL','XXL')])
    Color = models.CharField (max_length=50)
    Marca = models.CharField (max_length=50)
    PrecioCompra = models.FloatField ()    
    PrecioVenta = models.FloatField ()
    Stock = models.IntegerField () 
     
    def __str__(self) -> str:
        return f'{self.TipoProducto} - {self.Descripcion} - {self.Talle}'
    
    class Meta:
        ordering = ['TipoProducto', 'Descripcion']   
    
class Proveedor(models.Model):
    Nombre = models.CharField (max_length=50)
    Telefono = models.IntegerField ()
    Localidad = models.CharField (max_length=50)
    Email = models.CharField (max_length=50)

    def __str__(self) -> str:
        return self.Nombre
    
class Compra(models.Model):
    Proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    Fecha = models.DateField ()


class Vendedores(models.Model):
    Nombre = models.CharField (max_length=50)
    Telefono = models.IntegerField ()
    Direccion = models.CharField (max_length=50)

    def __str__(self) -> str:
        return self.Nombre

class Cliente(models.Model):
    Nombre = models.CharField (max_length=50)
    Telefono = models.IntegerField ()
    Direccion = models.CharField (max_length=50)
    Saldo = models.FloatField () 

    def __str__(self) -> str:
        return self.Nombre

class Ventas(models.Model):
    Vendedor = models.ForeignKey(Vendedores, on_delete=models.CASCADE)
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    TipoVenta = models.CharField (max_length=50)
    TipoPago = models.CharField (max_length=50)
    Fecha = models.DateField ()

class VentaProd(models.Model): 
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    Ventas = models.ForeignKey (Ventas, on_delete=models.CASCADE, related_name='ventaprod_set')  
    Cantidad = models.IntegerField (default=0)
    Total = models.DecimalField (max_digits=10, decimal_places=2, default=0.00)

class CompraProd(models.Model): 
    Compra=  models.ForeignKey(Compra, on_delete=models.CASCADE)
    Producto=  models.ForeignKey(Producto, on_delete=models.CASCADE)
    Cantidad = models.IntegerField (default=0)
    Total = models.DecimalField (max_digits=10, decimal_places=2, default=0.00)