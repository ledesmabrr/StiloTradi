from django.shortcuts import render, reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import Cliente,Compra,Producto,Proveedor,Vendedores,Ventas
from .forms import VendedoresForm

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

def listaProducto(request, pk):
    producto = producto.object.get(id=pk)
    context = {'Producto': Producto}
    return render(request, 'listaProducto.html', context)


def ProveedorModif(request,pk):
    proveedor=Proveedor.objects.get(id=pk)

    if request.method == 'POST':
        id = request.POST.get('id')
        nombre = request.POST.get('Nombre')
        telefono = request.POST.get('Telefono')
        localidad = request.POST.get('Localidad')
        email = request.POST.get('Email')

        proveedor.Nombre = nombre
        proveedor.Telefono = telefono
        proveedor.Localidad = localidad
        proveedor.Email = email
        proveedor.save()
        return HttpResponseRedirect(reverse('proveedor'))
    return render(request, "frmProveedor.html", {'proveedor': proveedor})


def ProveedorNuevo(request):
    if request.method== 'POST':
        nombre = request.POST.get('Nombre')
        telefono = request.POST.get('Telefono')
        localidad = request.POST.get('Localidad')
        email = request.POST.get('Email')
        Proveedor.objects.create(Nombre = nombre, Telefono = telefono, Localidad = localidad, Email = email)
        return HttpResponseRedirect(reverse('proveedor'))
    return render(request, "frmProveedor.html")


def ProveedorEliminar(request, pk):
    proveedor = Proveedor.objects.get(id=pk)
    if request.method == 'POST':
        proveedor.delete()
        return HttpResponseRedirect(reverse('proveedor'))
    return render(request, 'borrarProveedor.html', {'Proveedor': proveedor})

def VendedoresModif(request, pk):
    vendedores = Vendedores.objects.get(id=pk)
    if request.method == 'POST':
        form = VendedoresForm(request.POST, instance=vendedores)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('detalleVendedores'))
        else:
            form = VendedoresForm(instance=vendedores)
        return render(request, 'frmVendedores.html', {'form': form, 'vendedores': vendedores})
    
def VendedoresNuevo(request):
    if request.method == 'POST':
        form = VendedoresForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('detalleVendedores'))
        else:
            form = VendedoresForm()
        return render(request, 'frmVendedores.html', {'form': form})

def VendedoresEliminar(request, pk):
    vendedores = Proveedor.objects.get(id=pk)
    if request.method == 'POST':
        Vendedores.delete()
        return HttpResponseRedirect(reverse('detalleVendedores'))
    return render(request, 'frmVendedores.html', {'vendedores': vendedores})