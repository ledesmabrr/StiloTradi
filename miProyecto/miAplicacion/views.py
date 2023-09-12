from django.shortcuts import render, reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import Cliente,Compra,Producto,Proveedor,Vendedores,Ventas
from .forms import VendedoresForm, ClientesForm, ProductosForm, ProveedorForm 

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

''' View  frmProveedor Tipo de Formulario 1
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
'''

'''
def ProveedorNuevo(request):
    if request.method== 'POST':
        nombre = request.POST.get('Nombre')
        telefono = request.POST.get('Telefono')
        localidad = request.POST.get('Localidad')
        email = request.POST.get('Email')
        Proveedor.objects.create(Nombre = nombre, Telefono = telefono, Localidad = localidad, Email = email)
        return HttpResponseRedirect(reverse('proveedor'))
    return render(request, "frmProveedor.html")
'''
def ProveedorModif(request,pk):
    proveedor=Proveedor.objects.get(id=pk)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=Proveedor)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('proveedor'))
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'frmProveedor.html', {'form': form, 'proveedor': proveedor})
   


def ProveedorNuevo(request):
    if request.method == 'POST':
        form =ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('proveedor'))
    else:
        form = ProveedorForm()
    return render(request, 'frmProveedor.html', {'form': form})

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

def ClientesModif(request, pk):
    cliente = Cliente.objects.get(id=pk)
    if request.method == 'POST':
        form = ClientesForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cliente'))
    else:
        form = ClientesForm(instance=cliente)
    return render(request, 'frmClientes.html', {'form': form, 'cliente': cliente})
    
def ClientesNuevo(request):
    if request.method == 'POST':
        form = ClientesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cliente'))
    else:
        form = ClientesForm()
    return render(request, 'frmClientes.html', {'form': form})

def ClientesEliminar(request, pk):
    clientes = Cliente.objects.get(id=pk)
    if request.method == 'POST':
        clientes.delete()
        return HttpResponseRedirect(reverse('cliente'))
    return render(request, 'borrarCliente.html', {'clientes': clientes})

def ProductosModif(request, pk):
    producto = Producto.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductosForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('producto'))
    else:
        form = ProductosForm(instance=producto)
    return render(request, 'frmProductos.html', {'form': form, 'producto': producto})
    
def ProductosNuevo(request):
    if request.method == 'POST':
        form = ProductosForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('producto'))
    else:
        form = ProductosForm()
    return render(request, 'frmProductos.html', {'form': form})

def ProductosEliminar(request, pk):
    producto = Producto.objects.get(id=pk)
    if request.method == 'POST':
        producto.delete()
        return HttpResponseRedirect(reverse('producto'))
    return render(request, 'borrarProducto.html', {'producto': producto})