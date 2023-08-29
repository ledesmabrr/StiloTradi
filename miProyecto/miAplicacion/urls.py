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
               path('vendedores/vendedores/detalleVendedores/<int:pk>/', views.detalleVendedores, name='detalleProveedor'),
               path('cliente/cliente/detalleCliente/<int:pk>/', views.detalleCliente, name='detalleProveedor'),
               path('ventas/ventas/detalleVentas/<int:pk>/', views.detalleVentas, name='detalleVentas'),

               path('proveedor/NuevoProveedor/', views.ProveedorNuevo, name='ProveedorNuevo'),
               path('proveedor/ModificarProveedor/<int:pk>/', views.ProveedorModif, name='ProveedorModif'),
               path('proveedor/EliminarProveedor/<int:pk>/', views.ProveedorEliminar, name='ProveedorEliminar'),
               
               
                 
]   