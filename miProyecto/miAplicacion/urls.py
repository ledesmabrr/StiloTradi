from django.urls import path
from. import views
from django.views.generic import TemplateView


urlpatterns = [

               path('', views.index, name='index'),
               path('', views.main, name='main'), 
               
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

               path('get-product-price/<int:producto_id>/', views.get_precio_producto, name='get_product_price'),
               path('get-product-price-compra/<int:producto_id>/', views.get_precio_compra_producto, name='get_product_price-compra'),
               path('get-product-stock/<int:product_id>/', views.get_product_stock, name='get_product_stock'),

               path('ventas/VentasLista/', views.VentasLista.as_view(), name='ventasLista'), 
               path('ventas/VentasNuevo/', views.VentasNuevo.as_view(), name='ventasNuevo'),
               path('ventas/VentasModif/<int:pk>/', views.VentasModif.as_view(), name='VentasModif'),
               path('ventasPDF/<int:ventas_pk>', views.ventasPDF, name='ventasPDF'),

               path('compra/ComprasLista/', views.ComprasLista.as_view(), name='comprasLista'), 
               path('compra/CompraNuevo/', views.CompraNuevo.as_view(), name='CompraNuevo'),
               path('compra/CompraModif/<int:pk>/', views.CompraModif.as_view(), name='CompraModif'),
               path('comprasPDF/<int:compra_pk>/', views.comprasPDF, name='comprasPDF')               
            ]   
