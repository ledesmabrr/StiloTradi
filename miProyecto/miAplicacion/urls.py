from django.urls import path
from. import views


urlpatterns = [
               path('', views.main, name='main'),
               path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
               path('logout/', views.Logout, name='logout'),
               
               path('producto/', views.tabla_producto, name='producto'),
               path('proveedor/', views.tabla_proveedor, name='proveedor'),
               path('compra/', views.tabla_compra, name='compra'),
               path('vendedores/', views.tabla_vendedores, name='vendedores'),
               path('cliente/', views.tabla_cliente, name='cliente'),
               path('ventas/', views.tabla_ventas, name='ventas'),

               path('proveedor/ProveedorLista/', views.ProveedorLista.as_view(), name='proveedorLista'), 
               path('proveedor/ProveedorNuevo/', views.ProveedorNuevo.as_view(), name='ProveedorNuevo'),
               path('proveedor/ProveedorModif/<int:pk>/', views.ProveedorModif.as_view(), name='ProveedorModif'),
               path('proveedor/ProveedorBorrar/<int:pk>/', views.ProveedorBorrar.as_view(), name='ProveedorBorrar'),

               path('vendedores/VendedoresLista/', views.VendedoresLista.as_view(), name='vendedoresLista'),
               path('vendedores/NuevoVendedores/', views.VendedoresNuevo.as_view(), name='NuevoVendedores'),
               path('vendedores/VendedoresModif/<int:pk>/', views.VendedoresModif.as_view(), name='VendedoresModif'),
               path('vendedores/VendedoresBorrar/<int:pk>/', views.VendedoresBorrar.as_view(), name='VendedoresBorrar'),

               path('cliente/ClienteLista/', views.ClienteLista.as_view(), name='clienteLista'),
               path('cliente/ClienteNuevo/', views.ClienteNuevo.as_view(), name='ClienteNuevo'),
               path('cliente/ClienteModif/<int:pk>/', views.ClienteModif.as_view(), name='ClienteModif'),
               path('cliente/ClienteBorrar/<int:pk>/', views.ClienteBorrar.as_view(), name='ClienteBorrar'),

               path('producto/ProductoLista/', views.ProductoLista.as_view(), name='productoLista'),  
               path('producto/ProductoNuevo/', views.ProductoNuevo.as_view(), name='productoNuevo'),
               path('producto/ProductoModif/<int:pk>/', views.ProductoModif.as_view(), name='ProductoModif'),
               path('producto/ProductoBorrar/<int:pk>/', views.ProductoBorrar.as_view(), name='productoBorrar'),

               path('ventas/VentasLista/', views.VentasLista.as_view(), name='ventasLista'), 
               path('ventas/VentasNuevo/', views.VentasNuevo.as_view(), name='ventasNuevo'),
               path('ventas/VentasModif/<int:pk>/', views.VentasModif.as_view(), name='VentasModif'),

               path('compra/ComprasLista/', views.ComprasLista.as_view(), name='comprasLista'), 
               path('compra/CompraNuevo/', views.CompraNuevo.as_view(), name='ventasNuevo'),
               path('compra/CompraModif/<int:pk>/', views.CompraModif.as_view(), name='VentasModif'),

               path('login/main', views.main, name='main'),

              

               
]   
