import queue
from telnetlib import LOGOUT
from django.contrib.auth.mixins import PermissionRequiredMixin 
from django.shortcuts import redirect, render, reverse
from django.urls import reverse_lazy
from django.forms import formset_factory
from django.views.generic import CreateView, UpdateView, DeleteView, ListView,View
from django.http import HttpResponse,HttpResponseRedirect
from .models import Cliente,Compra,Producto,Proveedor,Vendedores,Ventas
from django.db.models import Q
from django.db.models import Sum
from .forms import VendedoresForm, ClientesForm, ProductosForm, ProveedorForm,VentasForm,CompraForm,VentaProdForm 
from django.contrib.auth.views import LoginView

#from .mixins import PermissionRequiredMixin

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
        TotalGeneral = Ventas.ventaprod_set.aggregate(total_sum= Sum("Total"))["total_sum"] or 0
        #TotalGeneral = Ventas.ventaprod_set.aggregate(sum("total"))["total__sum"] or 0
        context["TotalGeneral"] = TotalGeneral

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
        
def Logout(request):
    LOGOUT(request)
    return redirect('/index')


class PermissionRequiredMixin(View):
    permission_required = None
    login_url = '/login'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm(self.permission_required):
            return HttpResponseRedirect(self.login_url)
        return super().dispatch(request, *args, **kwargs)
    

