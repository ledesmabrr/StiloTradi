from django.urls import path
from. import views

urlpatterns = [
               path('', views.main, name='main'),
               path('producto/', views.tabla_producto, name='producto'),
               path('proveedor/', views.tabla_proveedor, name='proveedor'),
               path('compra/', views.tabla_compra, name='compra'),
               path('vendedores/', views.tabla_vendedores, name='vendedores'),
               path('cliente/', views.tabla_cliente, name='cliente'),
               path('ventas/', views.tabla_ventas, name='ventas'),
               path('producto/producto/detalleProducto/<int:pk>/', views.detalleProducto, name='detalleProducto'),
               path('proveedor/proveedor/detalleProveedor/<int:pk>/', views.detalleProveedor, name='detalleProveedor'),  
               path('compra/compra/detalleCompra/<int:pk>/', views.detalleCompra, name='detalleProveedor'),
               #path('vendedores/vendedores/detalleVendedores/<int:pk>/', views.detalleVendedores, name='detalleProveedor'),
               path('cliente/cliente/detalleCliente/<int:pk>/', views.detalleCliente, name='detalleProveedor'),
               #path('ventas/ventas/detalleVentas/<int:pk>/', views.detalleVentas, name='detalleVentas'),

               path('vendedores/NuevoVendedores/', views.VendedoresNuevo, name='VendedoresNuevo'),
               path('vendedores/ModificarVendedor/<int:pk>/', views.VendedoresModif, name='VendedoresModif'),
               path('vendedores/EliminarVendedor/<int:pk>/', views.VendedoresEliminar, name='VendedoresEliminar'),
               
               path('proveedor/ProveedorNuevo/', views.ProveedorNuevo.as_view(), name='ProveedorNuevo'),
               path('proveedor/ProveedorModif/<int:pk>/', views.ProveedorModif.as_view(), name='ProveedorModif'),
               path('proveedor/ProveedorBorrar/<int:pk>/', views.ProveedorBorrar.as_view(), name='ProveedorBorrar'),

               path('cliente/ClienteNuevo/', views.ClienteNuevo.as_view(), name='ClienteNuevo'),
               path('cliente/ClienteModif/<int:pk>/', views.ClienteModif.as_view(), name='ClienteModif'),
               path('cliente/ClienteBorrar/<int:pk>/', views.ClienteBorrar.as_view(), name='ClienteBorrar'),

              #path('producto/ProductoLista/', views.ProductoLista.as_view(), name='productoLista'),
               path('producto/ProductoNuevo/', views.ProductoNuevo.as_view(), name='productoNuevo'),
               path('producto/ProductoModif/<int:pk>/', views.ProductoModif.as_view(), name='productoModif'),
               path('producto/ProductoBorrar/<int:pk>/', views.ProductoBorrar.as_view(), name='productoBorrar'),
               
               path('ventas/VentasNuevo/', views.VentasNuevo.as_view(), name='ventasNuevo'),
               path('ventas/VentasModif/<int:pk>/', views.VentasModif.as_view(), name='VentasModif'),

               path('compra/CompraNuevo/', views.CompraNuevo.as_view(), name='ventasNuevo'),
               path('compra/CompraModif/<int:pk>/', views.CompraModif.as_view(), name='VentasModif'),
]   
