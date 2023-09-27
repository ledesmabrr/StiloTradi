from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.forms import formset_factory
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.http import HttpResponse,HttpResponseRedirect
from .models import Cliente,Compra,Producto,Proveedor,Vendedores,Ventas,VentaProd
from .forms import VendedoresForm, ClientesForm, ProductosForm, ProveedorForm,VentaProdForm,VentasForm,CompraForm   


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


def detalleProducto(request, pk):
    producto = Producto.objects.get(id=pk)
    context = {'producto': producto}
    return render(request, 'detalleProducto.html', context)

def detalleProveedor(request, pk):
    proveedor = Proveedor.objects.get(id=pk)
    context = {'proveedor': proveedor}
    return render(request, 'detalleProveedor.html', context)

def detalleCompra(request, pk):
    compra = Compra.objects.get(id=pk)
    context = {'compra': compra}
    return render(request, 'detalleCompra.html', context)

def detalleVendedores(request, pk):
    vendedores = Vendedores.objects.get(id=pk)
    context = {'vendedores': vendedores}
    return render(request, 'detalleVendedores.html', context)

def detalleCliente(request, pk):
    cliente = Cliente.objects.get(id=pk)
    context = {"cliente": cliente}
    return render(request, "detalleCliente.html",context)

def detalleVentas(request, pk):
    ventas = Ventas.objects.get(id=pk)
    context = {"ventas": ventas}
    return render(request, "detalleVentas.html",context)

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


def VendedoresModif(request, pk):
    vendedores = Vendedores.objects.get(id=pk)
    if request.method == 'POST':
        form = VendedoresForm(request.POST, instance=vendedores)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('vendedores'))
    else:
        form = VendedoresForm(instance=vendedores)
    return render(request, 'frmVendedores.html', {'form': form, 'vendedores': vendedores})
    
def VendedoresNuevo(request):
    if request.method == 'POST':
        form = VendedoresForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('vendedores'))
    else:
        form = VendedoresForm()
    return render(request, 'frmVendedores.html', {'form': form})

def VendedoresEliminar(request, pk):
    vendedores = Vendedores.objects.get(id=pk)
    if request.method == 'POST':
        vendedores.delete()
        return HttpResponseRedirect(reverse('vendedores'))
    return render(request, 'borrarVendedores.html', {'vendedores': vendedores})


class ProveedorLista(ListView):
    model = Proveedor
    template_name = 'Proveedor.html'
    context_object_name = 'proveedor'

class ProveedorNuevo(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'frmProveedor.html'
    success_url = reverse_lazy('proveedor')

class ProveedorModif(UpdateView):
    model = Proveedor 
    form_class = ProveedorForm
    template_name = 'frmProveedor.html'
    success_url = reverse_lazy('proveedor')

class ProveedorBorrar(DeleteView):
    model = Proveedor
    template_name = 'borrarProveedor.html'
    success_url = reverse_lazy('proveedor')


class ClienteLista(ListView):
    model = Cliente
    template_name = 'Cliente.html'
    context_object_name = 'cliente'

class ClienteNuevo(CreateView):
    model = Cliente
    form_class = ClientesForm
    template_name = 'frmClientes.html'
    success_url = reverse_lazy('cliente')

class ClienteModif(UpdateView):
    model = Cliente 
    form_class = ClientesForm
    template_name = 'frmClientes.html'
    success_url = reverse_lazy('cliente')

class ClienteBorrar(DeleteView):
    model = Cliente
    template_name = 'borrarCliente.html'
    success_url = reverse_lazy('cliente')


class ProductoLista(ListView):
    model = Producto
    template_name = 'Producto.html'
    context_object_name = 'productos'

class ProductoNuevo(CreateView):
    model = Producto
    form_class = ProductosForm
    template_name = 'frmProductos.html'
    success_url = reverse_lazy('producto')

class ProductoModif(UpdateView):
    model = Producto 
    form_class = ProductosForm
    template_name = 'frmProductos.html'
    success_url = reverse_lazy('producto')

class ProductoBorrar(DeleteView):
    model = Producto
    template_name = 'borrarProducto.html'
    success_url = reverse_lazy('producto')


class VentasNuevo(CreateView):
    model = Ventas
    form_class = VentasForm   
    template_name = 'VentaProd.html'
    success_url = reverse_lazy('ventas')

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
    success_url = reverse_lazy('ventas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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













class CompraNuevo(CreateView):
    model = Compra
    form_class = CompraForm   
    template_name = 'CompraProd.html'
    success_url = reverse_lazy('compra')

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
    success_url = reverse_lazy('compra')

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