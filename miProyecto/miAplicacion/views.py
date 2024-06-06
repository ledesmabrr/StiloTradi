from msilib import Table
from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.forms import formset_factory
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.http import HttpResponse,HttpResponseRedirect
from .models import Cliente,Compra,Producto,Proveedor,Vendedores,Ventas, CompraProd, VentaProd
from .forms import VendedoresForm, ClientesForm, ProductosForm, ProveedorForm,VentasForm,CompraForm,VentaProdForm 
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
from django.contrib.auth.views import LoginView, LogoutView 
from django.db.models import Sum

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
       
  
class VentasNuevo(CreateView):
    model = Ventas
    form_class = VentasForm   
    template_name = 'VentaProd.html'
    success_url = reverse_lazy('ventasLista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.POST:
            context['formset'] = VentasForm.VentaProdFormset(self.request.POST)
        else:
            context['formset'] = VentasForm.VentaProdFormset()
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid() and form.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))
        

class VentasModif(UpdateView):
    model = Ventas
    form_class = VentasForm
    template_name = 'VentaProd.html'
    success_url = reverse_lazy('ventasLista')

    def get_success_url(self) -> str:
        return self.request.path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        Ventas = self.object
        total = Ventas.VentaProd_set.aggregate(total_sum= Sum("Total"))["total_sum"] or 0
        #TotalGeneral = Ventas.ventaprod_set.aggregate(sum("total"))["total__sum"] or 0
        context["TotalGeneral"] = total

        if self.request.POST:
            context['formset'] = VentasForm.VentaProdFormset(self.request.POST, instance=self.object)
        else:
            context['formset'] = VentasForm.VentaProdFormset(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid() and form.is_valid():
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))

class VentasLista(ListView):
    model = Ventas
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
        if self.request.POST:
            context['formset'] = CompraForm.CompraProdFormset(self.request.POST)
        else:
            context['formset'] = CompraForm.CompraProdFormset()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid() and form.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))


class CompraModif(UpdateView):
    model = Compra
    form_class = CompraForm
    template_name = 'CompraProd.html'
    success_url = reverse_lazy('comprasLista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = CompraForm.CompraProdFormset(self.request.POST, instance=self.object)
        else:
            context['formset'] = CompraForm.CompraProdFormset(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid() and form.is_valid():
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))


def ventasPDF(request, venta_pk):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)

    venta_prods = VentaProd.objects.filter(Ventas__pk=venta_pk)

    # Configura el buffer y el lienzo
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=letter)

    textobj = c.beginText()
    textobj.setTextOrigin(inch, inch)
    textobj.setFont("Helvetica", 14)

    # Configura estilos
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    normal_style = styles['Normal']

    # Contenido del PDF
    content = []

  
    # Agrega título con la PK de la compra
    title_text = f"Detalle de venta número: {venta_pk}"
    title = Paragraph(title_text, title_style)
    content.append(title)

    for venta_prods in venta_prods:
        # Detalles de Producto y Cantidad para cada compra

        product_and_quantity_details = [
            f'<b>Producto:</b> {venta_prods.Producto} <b>Cantidad:</b> {venta_prods.Cantidad}',
                " ",  # Espacio entre cada instancia
        ]
        content.extend([Paragraph(detail, normal_style) for detail in product_and_quantity_details])

    # Detalles únicos (Compra y Fecha)
    unique_details_added = False
    for venta_prod in venta_prods:
        if not unique_details_added:
            unique_details = [
                f'<b>Vendedor:</b> {venta_prods.Ventas.Vendedor}',
                f'<b>Cliente:</b> {venta_prods.Ventas.Cliente}',
                f'<b>TipoVenta:</b> {venta_prods.Ventas.TipoVenta}',
                f'<b>TipoPago:</b> {venta_prods.Ventas.TipoPago}',
                f'<b>Fecha:</b> {venta_prods.Ventas.Fecha}',
                f'<b>Total:</b> {venta_prods.Total}',
                    " ",  # Espacio entre cada instancia
            ]
             # Agrega detalles únicos al contenido
            content.extend([Paragraph(detail, normal_style) for detail in unique_details])
        unique_details_added = True

    title_text = f"Gracias por su compra"
    title = Paragraph(title_text, title_style)
    content.append(title)

    title_text = f"StiloTradi"
    title = Paragraph(title_text, title_style)
    content.append(title)

    
      # Construye el PDF
    doc.build(content)

    # Envia el PDF como respuesta
    buf.seek(0)

    c.drawText(textobj)
    c.showPage()
    c.save()
    buf.seek(0)

    response = FileResponse(buf, as_attachment=True, filename=f'venta_{venta_pk}.pdf')
    return response






def comprasPDF(request, compra_pk):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)

    compra_prods = CompraProd.objects.filter(Compra__pk=compra_pk)

    # Configura el buffer y el lienzo
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=letter)

    textobj = c.beginText()
    textobj.setTextOrigin(inch, inch)
    textobj.setFont("Helvetica", 14)

    # Configura estilos
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    normal_style = styles['Normal']

    # Contenido del PDF
    content = []

  
    # Agrega título con la PK de la compra
    title_text = f"Detalle de compra número: {compra_pk}"
    title = Paragraph(title_text, title_style)
    content.append(title)

    for compra_prod in compra_prods:
        # Detalles de Producto y Cantidad para cada compra

        product_and_quantity_details = [
            f'<b>Producto:</b> {compra_prod.Producto} <b>Cantidad:</b> {compra_prod.Cantidad}',
                " ",  # Espacio entre cada instancia
        ]
        content.extend([Paragraph(detail, normal_style) for detail in product_and_quantity_details])

    # Detalles únicos (Compra y Fecha)
    unique_details_added = False
    for compra_prod in compra_prods:
        if not unique_details_added:
            unique_details = [
                f'<b>Proveedor:</b> {compra_prod.Compra.Proveedor}',
                f'<b>Fecha:</b> {compra_prod.Compra.Fecha}',
                f'<b>Total:</b> {compra_prod.Total}',
                    " ",  # Espacio entre cada instancia
            ]
             # Agrega detalles únicos al contenido
            content.extend([Paragraph(detail, normal_style) for detail in unique_details])
        unique_details_added = True

    
      # Construye el PDF
    doc.build(content)

    # Envia el PDF como respuesta
    buf.seek(0)

    c.drawText(textobj)
    c.showPage()
    c.save()
    buf.seek(0)

    response = FileResponse(buf, as_attachment=True, filename=f'compra_{compra_pk}.pdf')
    return response

def index(request):
    return render(request, 'index.html')


