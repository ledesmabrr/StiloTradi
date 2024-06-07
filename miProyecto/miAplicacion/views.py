from ast import Yield
from calendar import c
from cgitb import text
import colorsys
from msilib import Table
from pyexpat.errors import messages
from urllib import request
import xdrlib
from django.shortcuts import redirect, render, reverse
from django.urls import reverse_lazy
from django.forms import formset_factory, inlineformset_factory
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from .models import Cliente,Compra,Producto,Proveedor,Vendedores,Ventas, CompraProd, VentaProd
from .forms import CompraProdForm, VendedoresForm, ClientesForm, ProductosForm, ProveedorForm,VentasForm,CompraForm,VentaProdForm 
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from django.shortcuts import get_object_or_404
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph,Table, TableStyle
from reportlab.platypus import Paragraph
from django.contrib.auth.views import LoginView, LogoutView 
from django.db.models import Sum
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def main(request):
    producto = Producto.objects.all()
    proveedor = Proveedor.objects.all()
    compra = Compra.objects.all()
    vendedores = Vendedores.objects.all()
    cliente = Cliente.objects.all()
    ventas = Ventas.objects.all()

    context = {'producto': producto,
               'proveedor': proveedor,
               'compra': compra,
               'vendedores': vendedores,
               'cliente': cliente,
               'ventas':ventas}
    
    return render(request, 'main.html', context)



def tabla_cliente(request):
    cliente = Cliente.objects.all()
    context = {'cliente': cliente}
    return render(request, 'cliente.html', context)

def tabla_producto(request):
    producto = Producto.objects.all()
    context = {'producto': producto}
    return render(request, 'producto.html', context)

def tabla_proveedor(request):
    proveedor = Proveedor.objects.all()
    context = {'proveedor': proveedor}
    return render(request, 'proveedor.html', context)

def tabla_vendedores(request):
    vendedores = Vendedores.objects.all()
    context = {'vendedores': vendedores}
    return render(request, 'vendedores.html', context)

def tabla_compra(request):
    compra = Compra.objects.all()
    context = {'compra': compra}
    return render(request, 'compra.html', context)

def tabla_ventas(request):
    ventas = Ventas.objects.all()
    context = {'ventas': ventas}
    return render(request, 'ventas.html', context)


def index(request):
    mensaje=f"<html><h2>Bienvenidos a Stilo Tradi</h2>"\
    f"<p>Este es un sistema de venta de ropa</p>"
    return HttpResponse(mensaje)

class VendedoresModif(UpdateView):
    model = Vendedores 
    form_class = VendedoresForm
    template_name = 'frmVendedores.html'
    success_url = reverse_lazy('vendedoresLista')

    
class VendedoresNuevo(CreateView):
    model = Vendedores
    form_class = VendedoresForm
    template_name = 'frmVendedores.html'
    success_url = reverse_lazy('vendedoresLista')

class VendedoresBorrar(DeleteView):
    model = Vendedores
    template_name = 'borrarVendedores.html'
    success_url = reverse_lazy('vendedoresLista')


class VendedoresLista(ListView):
    model = Vendedores
    template_name = 'Vendedores.html'
    context_object_name = 'vendedores'
    paginate_by = 3  # Cantidad de elementos por página

    def get_queryset(self):
        query = self.request.GET.get('q', '')

        if not query: 
            vendedores = Vendedores.objects.all()
        else:
            vendedores = Vendedores.objects.filter(Nombre__icontains = query)
        return vendedores

class ProveedorLista(ListView):
    model = Proveedor
    template_name = 'Proveedor.html'
    context_object_name = 'proveedor'
    paginate_by = 3  # Cantidad de elementos por página

    def get_queryset(self):
        query = self.request.GET.get('q', '')

        if not query: 
            proveedor = Proveedor.objects.all()
        else:
            proveedor = Proveedor.objects.filter(Nombre__icontains = query)
        return proveedor

class ProveedorNuevo(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'frmProveedor.html'
    success_url = reverse_lazy('proveedorLista')

class ProveedorModif(UpdateView):
    model = Proveedor 
    form_class = ProveedorForm
    template_name = 'frmProveedor.html'
    success_url = reverse_lazy('proveedorLista')

class ProveedorBorrar(DeleteView):
    model = Proveedor
    template_name = 'borrarProveedor.html'
    success_url = reverse_lazy('proveedorLista')


class ClienteLista(ListView):
    model = Cliente
    template_name = 'Cliente.html'
    context_object_name = 'cliente'
    paginate_by = 3

    def get_queryset(self):
        query = self.request.GET.get('q', '')

        if not query: 
            cliente = Cliente.objects.all()
        else:
            cliente = Cliente.objects.filter(Nombre__icontains = query)
        return cliente
    
class ClienteNuevo(CreateView):
    model = Cliente
    form_class = ClientesForm
    template_name = 'frmClientes.html'
    success_url = reverse_lazy('clienteLista')

class ClienteModif(UpdateView):
    model = Cliente 
    form_class = ClientesForm
    template_name = 'frmClientes.html'
    success_url = reverse_lazy('clienteLista')

class ClienteBorrar(DeleteView):
    model = Cliente
    template_name = 'borrarCliente.html'
    success_url = reverse_lazy('clienteLista')

class ProductoNuevo(CreateView):
    model = Producto
    form_class = ProductosForm
    template_name = 'frmProductos.html'
    success_url = reverse_lazy('productoLista')

class ProductoModif(UpdateView):
    model = Producto 
    form_class = ProductosForm
    template_name = 'frmProductos.html'
    success_url = reverse_lazy('productoLista')
    #permission_required = 'app.change_Producto'


class ProductoBorrar(DeleteView):
    model = Producto
    template_name = 'borrarProducto.html'
    success_url = reverse_lazy('productoLista')

class ProductoLista(ListView):
    model = Producto
    template_name = 'producto.html'
    context_object_name = 'productos'
    paginate_by =  3 # Cantidad de elementos por página

    def get_queryset(self):
        query = self.request.GET.get('q', '')

        if not query: 
            productos = Producto.objects.all()
        else:
            productos = Producto.objects.filter(TipoProducto__icontains = query)
        return productos
       



def get_precio_producto(request, producto_id):
    try:
        producto = Producto.objects.get(pk=producto_id)
        precio = producto.PrecioVenta  # Ajusta esto según el nombre del campo en tu modelo Producto
        return JsonResponse({'precio': precio})
    except Producto.DoesNotExist:
        return JsonResponse({'error': 'El producto no existe'}, status=404)


def get_precio_compra_producto(request, producto_id):
    try:
        producto = Producto.objects.get(pk=producto_id)
        precioCompra = producto.PrecioCompra  # Ajusta esto según el nombre del campo en tu modelo Producto
        return JsonResponse({'precioCompra': precioCompra})
    except Producto.DoesNotExist:
        return JsonResponse({'error': 'El producto no existe'}, status=404)




class VentasNuevo(CreateView):
    model = Ventas
    form_class = VentasForm   
    template_name = 'VentaProd.html'
    success_url = reverse_lazy('ventasLista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        formset = self.get_VentaProdFormset(data=self.request.POST if self.request.method == 'POST' else None, instance=self.object)
        context['formset'] = formset

        # Obtener el precio de venta del producto seleccionado y pasarlo al formulario VentaProdForm
        producto_id = self.request.POST.get('Producto', None)
        if producto_id:
            producto = Producto.objects.get(pk=producto_id)
            precio_venta = producto.PrecioVenta
            context['precio_venta'] = precio_venta

        # Calcular el total solo si el formset es válido
        if formset.is_valid():
            total = sum(float(form.cleaned_data.get('SubTotal', 0)) for form in formset.forms if form.is_valid())
            context['total'] = total
        else:
            print("Formset no válido:", formset.errors)
            context['total'] = 0

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        if formset.is_valid() and form.is_valid():
            # Guardar el formulario principal
            self.object = form.save()

            # Guardar los objetos VentaProd asociados
            for venta_prod_form in formset:
                if venta_prod_form.cleaned_data:
                    venta_prod_form.instance.Ventas = self.object
                    venta_prod_form.save()

                    # Descontar el stock de cada producto vendido
                    producto = venta_prod_form.cleaned_data['Producto']
                    cantidad_vendida = venta_prod_form.cleaned_data['Cantidad']
                    producto.Stock -= cantidad_vendida
                    producto.save()

            # Calcular y guardar el total en el formulario Ventas
            total = sum(float(form.cleaned_data.get('SubTotal', 0)) for form in formset.forms if form.is_valid() and form.cleaned_data.get('SubTotal') is not None)
            self.object.Total = total
            self.object.save()

            print("Total de la venta:", total)

            # Realiza la acción necesaria después de que el formulario es válido
            print("Venta guardada correctamente:", self.object)
            return super().form_valid(form)
        else:
            print("Formulario principal inválido: ", form.errors)
            print("Formset inválido: ", formset.errors)
            return self.render_to_response(self.get_context_data(form=form))

    def get_VentaProdFormset(self, data=None, instance=None):
        return inlineformset_factory(Ventas, VentaProd, form=VentaProdForm, extra=5, can_delete=True, min_num=1)(data, instance=instance)











class VentasModif(UpdateView):
    model = Ventas
    form_class = VentasForm
    template_name = 'VentaProd.html'
    success_url = reverse_lazy('ventasLista')

    def get_success_url(self) -> str:
        return self.request.path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        formset = self.get_VentaProdFormset(data=self.request.POST if self.request.method == 'POST' else None, instance=self.object)
        context['formset'] = formset
        context['form'] = self.get_form()

        # Obtener el precio de venta del producto seleccionado y pasarlo al formulario VentaProdForm
        producto_id = self.request.POST.get('Producto', None)
        if producto_id:
            producto = Producto.objects.get(pk=producto_id)
            precio_venta = producto.PrecioVenta
            context['precio_venta'] = precio_venta

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        if formset.is_valid() and form.is_valid():
            # Guardar el formulario principal
            self.object = form.save()
            subtotals = []
            # Guardar los objetos VentaProd asociados
            for venta_prod_form in formset:
                if venta_prod_form.cleaned_data:
                    venta_prod_form.instance.Ventas = self.object
                    venta_prod_form.save()

                    # Descontar el stock de cada producto vendido
                    producto = venta_prod_form.cleaned_data['Producto']
                    cantidad_vendida = venta_prod_form.cleaned_data['Cantidad']
                    producto.Stock -= cantidad_vendida
                    producto.save()

             # Recalcular y guardar el total en el formulario Ventas
            total_anterior = float(self.object.Total)
            total_nuevo = sum(float(form.cleaned_data['SubTotal']) for form in formset.forms if form.is_valid() and form.cleaned_data.get('SubTotal') is not None)
            total = total_anterior + total_nuevo
            self.object.Total = total
            self.object.save()

            # Realiza la acción necesaria después de que el formulario es válido
            print("Venta guardada correctamente:", self.object)
            return super().form_valid(form)
        else:
            print("Formulario principal inválido: ", form.errors)
            print("Formset inválido: ", formset.errors)
            return self.render_to_response(self.get_context_data(form=form))
        
    def get_VentaProdFormset(self, data=None, instance=None):
        formset = inlineformset_factory(Ventas, VentaProd, form=VentaProdForm, extra=5, can_delete=True, min_num=1, fields=('Ventas','Producto', 'Cantidad', 'PrecioVenta', 'SubTotal'))(data, instance=instance)

        # Obtener el precio de venta del producto seleccionado y pasarlo al formulario VentaProdForm
        if instance and instance.pk:
            for form in formset.forms:
                if form.instance.pk:
                    producto_id = form.instance.Producto.pk
                    producto = Producto.objects.get(pk=producto_id)
                    form.initial['PrecioVenta'] = producto.PrecioVenta
        
        return formset








class VentasLista(ListView):
    model = Ventas
    ordering = ['-id']  # Ordena por id de manera descendente
    template_name = 'ventas.html'
    context_object_name = 'ventas'
    paginate_by = 3

    #def get_queryset(self):
        #query = self.request.GET.get('q')
        #if query:
            #return Ventas.objects.filter(Fecha__startswith=query)
        #return Ventas.objects.all()
    

    def get_queryset(self):
        query = self.request.GET.get('q', '')

        if not query: 
            ventas = Ventas.objects.all()
        else:
            ventas = Ventas.objects.filter(Fecha__startswith = query)
        return ventas
    
    
class ComprasLista(ListView):
    model = Compra
    ordering = ['-id']  # Ordena por id de manera descendente
    template_name = 'compra.html'
    context_object_name = 'compra'
    paginate_by = 3

    #def get_queryset(self):
     #  query = self.request.GET.get('q')
      # if query:
            #return Compra.objects.filter(Fecha__startswith=query)
        #return Compra.objects.all()    
    
    def get_queryset(self):
        query = self.request.GET.get('q', '')

        if not query: 
            compra = Compra.objects.all()
        else:
            compra = Compra.objects.filter(Fecha__startswith = query)
        return compra
    


    
class CompraNuevo(CreateView):
    model = Compra
    form_class = CompraForm   
    template_name = 'CompraProd.html'
    success_url = reverse_lazy('comprasLista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        formset = self.get_CompraProdFormset(data=self.request.POST if self.request.method == 'POST' else None, instance=self.object)
        context['formset'] = formset

        # Obtener el precio de venta del producto seleccionado y pasarlo al formulario VentaProdForm
        producto_id = self.request.POST.get('Producto', None)
        if producto_id:
            producto = Producto.objects.get(pk=producto_id)
            precio_compra = producto.PrecioCompra
            context['precio_compra'] = precio_compra

        # Calcular el total solo si el formset es válido
        if formset.is_valid():
            total = sum(float(form.cleaned_data.get('SubTotal', 0)) for form in formset.forms if form.is_valid())
            context['total'] = total
        else:
            print("Formset no válido:", formset.errors)
            context['total'] = 0

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        if formset.is_valid() and form.is_valid():
            # Guardar el formulario principal
            self.object = form.save()

            # Guardar los objetos VentaProd asociados
            for compra_prod_form in formset:
                if compra_prod_form.cleaned_data:
                    compra_prod_form.instance.Compra = self.object
                    compra_prod_form.save()

                    # # Descontar el stock de cada producto vendido
                    # producto = compra_prod_form.cleaned_data['Producto']
                    # cantidad_vendida = compra_prod_form.cleaned_data['Cantidad']
                    # producto.Stock -= cantidad_vendida
                    # producto.save()

            # Calcular y guardar el total en el formulario Ventas
            total = sum(float(form.cleaned_data.get('SubTotal', 0)) for form in formset.forms if form.is_valid() and form.cleaned_data.get('SubTotal') is not None)
            self.object.Total = total
            self.object.save()

            print("Total de la compra:", total)

            # Realiza la acción necesaria después de que el formulario es válido
            print("Compra guardada correctamente:", self.object)
            return super().form_valid(form)
        else:
            print("Formulario principal inválido: ", form.errors)
            print("Formset inválido: ", formset.errors)
            return self.render_to_response(self.get_context_data(form=form))

    def get_CompraProdFormset(self, data=None, instance=None):
        return inlineformset_factory(Compra, CompraProd, form=CompraProdForm, extra=5, can_delete=True, min_num=1)(data, instance=instance)



class CompraModif(UpdateView):
    model = Compra
    form_class = CompraForm
    template_name = 'CompraProd.html'
    success_url = reverse_lazy('comprasLista')

    def get_success_url(self) -> str:
        return self.request.path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        formset = self.get_CompraProdFormset(data=self.request.POST if self.request.method == 'POST' else None, instance=self.object)
        context['formset'] = formset
        context['form'] = self.get_form()

        # Obtener el precio de venta del producto seleccionado y pasarlo al formulario VentaProdForm
        producto_id = self.request.POST.get('Producto', None)
        if producto_id:
            producto = Producto.objects.get(pk=producto_id)
            precio_compra = producto.PrecioCompra
            context['precio_compra'] = precio_compra

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        if formset.is_valid() and form.is_valid():
            # Guardar el formulario principal
            self.object = form.save()

            # Guardar los objetos VentaProd asociados
            for compra_prod_form in formset:
                if compra_prod_form.cleaned_data:
                    compra_prod_form.instance.Compra = self.object
                    compra_prod_form.save()

                    # # Descontar el stock de cada producto vendido
                    # producto = compra_prod_form.cleaned_data['Producto']
                    # cantidad_vendida = compra_prod_form.cleaned_data['Cantidad']
                    # producto.Stock -= cantidad_vendida
                    # producto.save()

             # Recalcular y guardar el total en el formulario Ventas
            total_anterior = float(self.object.Total)
            total_nuevo = sum(float(form.cleaned_data['SubTotal']) for form in formset.forms if form.is_valid() and form.cleaned_data.get('SubTotal') is not None)
            total = total_anterior + total_nuevo
            self.object.Total = total
            self.object.save()

            # Realiza la acción necesaria después de que el formulario es válido
            print("Compra guardada correctamente:", self.object)
            return super().form_valid(form)
        else:
            print("Formulario principal inválido: ", form.errors)
            print("Formset inválido: ", formset.errors)
            return self.render_to_response(self.get_context_data(form=form))
        
    def get_CompraProdFormset(self, data=None, instance=None):
        formset = inlineformset_factory(Compra, CompraProd, form=CompraProdForm, extra=5, can_delete=True, min_num=1, fields=('Compra','Producto', 'Cantidad', 'PrecioCompra', 'SubTotal'))(data, instance=instance)

        # Obtener el precio de venta del producto seleccionado y pasarlo al formulario VentaProdForm
        if instance and instance.pk:
            for form in formset.forms:
                if form.instance.pk:
                    producto_id = form.instance.Producto.pk
                    producto = Producto.objects.get(pk=producto_id)
                    form.initial['PrecioCompra'] = producto.PrecioCompra
        
        return formset

def ventasPDF(request, ventas_pk):
    # Configura el buffer y el lienzo
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter)
    doc = SimpleDocTemplate(buf, pagesize=letter)

    venta_prods = VentaProd.objects.filter(Ventas__pk=ventas_pk)
    # Configura estilos
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    normal_style = styles['Normal']

    # Contenido del PDF
    content = []

    # Agrega título con el nombre de la tienda
    title_text = f"Stilo Tradi"
    title = Paragraph(title_text, title_style)
    content.append(title)

    # Detalles de la venta
    text_lines = [
        "Libertad 275 San Pedro (5870), Cordoba",
        "",
        "Factura simplificada",
        f"Fecha: {venta_prods.first().Ventas.Fecha if venta_prods.exists() else 'Fecha no disponible'}",  # Obtener la fecha de la primera venta si existe
        f"Detalle de venta número: {ventas_pk}",
        "-----------------------------------------------------------------"

    ]

    for line in text_lines:
        paragraph = Paragraph(line, normal_style)
        content.append(paragraph)


    # Encabezado de la tabla
    header = [
        Paragraph("<b>Producto</b>", normal_style),
        Paragraph("<b>Cantidad</b>", normal_style),
        Paragraph("<b>Precio</b>", normal_style),
        Paragraph("<b>Subtotal</b>", normal_style)
    ]   

    # Detalles de Producto, Cantidad y precio para cada compra
    product_and_quantity_details = []
    total_venta = 0  # Inicializa el total de la venta
    for venta_prod in venta_prods:
        product_and_quantity_details.append([
            venta_prod.Producto,
            venta_prod.Cantidad,
            venta_prod.Producto.PrecioVenta,
            venta_prod.SubTotal
            #agregar el precio
        ])
        total_venta += venta_prod.SubTotal
        # total_venta = venta_prod.Ventas.Total

    # Agrega el encabezado a la lista de detalles
    product_and_quantity_details.insert(0, header)

   # Agrega el total al final de los detalles
    total_paragraph = Paragraph(f"<b>Total: {venta_prod.Ventas.Total}</b>", normal_style)
    product_and_quantity_details.append(["", "", "", total_paragraph])

     # Configura el estilo de la tabla
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Fondo gris para el encabezado
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),  # Texto blanco para el encabezado
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),  # Tipo de fuente
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),  # Alineación izquierda 
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),  # Alineación vertical superior
    ])

    # Crea la tabla con los detalles de producto y cantidad
    table = Table(product_and_quantity_details)

    # Aplica el estilo a la tabla
    table.setStyle(table_style)

    # Detalles únicos (Compra y Fecha)
    unique_details_added = False
    for venta_prod in venta_prods:
        if not unique_details_added:
            unique_details = [
                Paragraph(f'<b>Vendedor:</b> {venta_prod.Ventas.Vendedor}', normal_style),
                Paragraph(f'<b>Cliente:</b> {venta_prod.Ventas.Cliente}', normal_style),
                Paragraph(f'<b>TipoVenta:</b> {venta_prod.Ventas.TipoVenta}', normal_style),
                Paragraph(f'<b>TipoPago:</b> {venta_prod.Ventas.TipoPago}', normal_style),
            ]
            # Agrega detalles únicos al contenido
            content.extend(unique_details)
            content.append(Paragraph("-----------------------------------------------------------------", normal_style))  # Agregar separador de línea
            unique_details_added = True
    
    # Agrega la tabla al contenido del PDF
    content.append(table)
   # Mensaje de agradecimiento
    thank_you_text = f"Gracias por su compra"
    thank_you = Paragraph(thank_you_text, title_style)
    content.append(thank_you)

    # Construye el PDF
    doc.build(content)

    # Envía el PDF como respuesta
    buf.seek(0)
    response = FileResponse(buf, as_attachment=True, filename=f'venta_{ventas_pk}.pdf')
    return response






def comprasPDF(request, compra_pk):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    doc = SimpleDocTemplate(buf, pagesize=letter)

    compra_prods = CompraProd.objects.filter(Compra__pk=compra_pk)

    # Configura estilos
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    normal_style = styles['Normal']

    # Contenido del PDF
    content = []

    # Agrega título con el nombre de la tienda
    title_text = f"Stilo Tradi"
    title = Paragraph(title_text, title_style)
    content.append(title)

    # Detalles de la compra
    text_lines = [
        "Factura simplificada",
        f"Fecha: {compra_prods.first().Compra.Fecha if compra_prods.exists() else 'Fecha no disponible'}", 
        f"Proveedor: {compra_prods.first().Compra.Proveedor }",
        f"Detalle de compra número: {compra_pk}",
        "-------------------------------------------"
    ]

    for line in text_lines:
        paragraph = Paragraph(line, normal_style)
        content.append(paragraph)

    # Agrega la tabla al contenido del PDF
    content.append(Paragraph(" ", normal_style))  # Salto de línea antes de la tabla

    # Encabezado de la tabla
    header = [
        Paragraph("<b>Producto</b>", normal_style),
        Paragraph("<b>Cantidad</b>", normal_style),
        Paragraph("<b>Precio de Compra</b>", normal_style),
        Paragraph("<b>Subtotal</b>", normal_style)
    ]   

    # Detalles de Producto, Cantidad y precio para cada compra
    product_and_quantity_details = []
    total_compra = 0  # Inicializa el total de la venta
    for compra_prod in compra_prods:
        product_and_quantity_details.append([
            compra_prod.Producto,
            compra_prod.Cantidad,
            compra_prod.Producto.PrecioCompra,
            compra_prod.SubTotal
        ])
        total_compra += compra_prod.SubTotal

    # Agrega el encabezado a la lista de detalles
    product_and_quantity_details.insert(0, header)

    # Agrega el total al final de los detalles
    total_paragraph = Paragraph(f"<b>Total: {compra_prod.Compra.Total}</b>", normal_style)
    product_and_quantity_details.append(["", "", "", total_paragraph])

    # Configura el estilo de la tabla
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Fondo gris para el encabezado
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),  # Texto blanco para el encabezado
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),  # Tipo de fuente
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),  # Alineación izquierda 
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),  # Alineación vertical superior
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Borde para todas las celdas
    ])

    # Crea la tabla con los detalles de producto y cantidad
    table = Table(product_and_quantity_details)

    # Aplica el estilo a la tabla
    table.setStyle(table_style)

    # Agrega la tabla al contenido del PDF
    content.append(table)
    
    # Construye el PDF
    doc.build(content)

    # Envia el PDF como respuesta
    buf.seek(0)
    response = FileResponse(buf, as_attachment=True, filename=f'compra_{compra_pk}.pdf')
    return response


def index(request):
    return render(request, 'index.html')

def get_product_stock(request, product_id):
    try:
        product = Producto.objects.get(pk=product_id)
        stock = product.Stock
        return JsonResponse({'stock': stock})
    except Producto.DoesNotExist:
        return JsonResponse({'error': 'Producto no encontrado'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirige al usuario a la página que quieras
            return redirect('/base')
        else:
            # Muestra un mensaje de error si las credenciales son incorrectas
            messages.error(request, 'Usuario o contraseña incorrectos')
            return redirect('/login')
    else:
        return render(request, 'login.html')