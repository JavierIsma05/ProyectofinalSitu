from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import Http404
 
from .forms import CustomUserCreationForm
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.

def home_view(request):
    return render(request,"app/home.html",{})

def about_view(request):
    return render(request,"app/about.html",{})

''' GESTIONAR BUSES'''
def buses(request):    
    buseslistados = Bus.objects.all()
    page = request.GET.get('page',1)
    
    try:
        paginator = Paginator(buseslistados,5)
        buseslistados = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity': buseslistados,
        'paginator': paginator
    }
    return render(request,"app/buses/gestionarBuses.html",data)

def registrarBus(request):
    placa = request.POST['txtPlaca']
    modelo = request.POST['txtModelo']
    capacidad_pasajeros = request.POST['txtCapacidad']

    usuario = Bus.objects.create(placa=placa,modelo=modelo,capacidad_pasajeros=capacidad_pasajeros)
    messages.success(request, '¡Bus registrado!')
    return redirect('/buses')

 
def edicionBus(request, codigo):
    usuario = Bus.objects.get(codigo=codigo)
    return render(request, "app/buses/edicionBus.html", {"usuario": usuario})

def editarBus(request):
    placa = request.POST['txtPlaca']
    modelo = request.POST['txtModelo']
    capacidad_pasajeros = request.POST['txtCapacidad']

    usuario = Bus.objects.get(codigo=placa)
    '''usuario.placa = placa'''
    usuario.modelo = modelo
    usuario.capacidad_pasajeros = capacidad_pasajeros
    usuario.save()

    messages.success(request, '¡Bus actualizado!')

    return redirect('/buses')

def eliminarBus(request, placa):
    usuario = Bus.objects.get(codigo=placa)
    usuario.delete()

    messages.success(request, "¡Bus eliminado!")

    return redirect('/buses')

''' GESTIONAR PASAJEROS'''
def pasajeros(request):    
    pasajeroslistados = Pasajero.objects.all()
    page = request.GET.get('page',1)
    
    try:
        paginator = Paginator(pasajeroslistados,5)
        pasajeroslistados = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity': pasajeroslistados,
        'paginator': paginator
    }
    return render(request,"app/pasajero/gestionarPasajeros.html",data)

def registrarPasajero(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    
    usuario = Pasajero.objects.create(codigo=codigo,nombre=nombre)
    messages.success(request, '¡Pasajero registrado!')
    return redirect('/buses')

 
def edicionPasajero(request, codigo):
    usuario = Pasajero.objects.get(codigo=codigo)
    return render(request, "app/pasajero/edicionPasajero.html", {"usuario": usuario})

def editarPasajero(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']

    usuario = Pasajero.objects.get(codigo=codigo)
    usuario.codigo = codigo
    usuario.nombre = nombre
    usuario.save()

    messages.success(request, '¡Pasajero actualizado!')

    return redirect('/pasajeros')

def eliminarPasajero(request, codigo):
    usuario = Pasajero.objects.get(codigo=codigo)
    usuario.delete()

    messages.success(request, "¡Pasajero eliminado!")

    return redirect('/pasajeros')

''' GESTOINAR VIAJES '''
def viajes(request):    
    viajeslistaados = Viaje.objects.all()
    page = request.GET.get('page',1)
    
    try:
        paginator = Paginator(viajeslistaados,5)
        viajeslistaados = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity': viajeslistaados,
        'paginator': paginator
    }
    return render(request,"app/viaje/gestionarViajes.html",data)

def registrarViaje(request):
   
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    
    usuario = Pasajero.objects.create(codigo=codigo,nombre=nombre)
    messages.success(request, '¡Pasajero registrado!')
    return redirect('/buses')

 
def edicionPasajero(request, codigo):
    usuario = Pasajero.objects.get(codigo=codigo)
    return render(request, "app/pasajero/edicionPasajero.html", {"usuario": usuario})

def editarPasajero(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']

    usuario = Pasajero.objects.get(codigo=codigo)
    usuario.codigo = codigo
    usuario.nombre = nombre
    usuario.save()

    messages.success(request, '¡Pasajero actualizado!')

    return redirect('/pasajeros')

def eliminarPasajero(request, codigo):
    usuario = Pasajero.objects.get(codigo=codigo)
    usuario.delete()

    messages.success(request, "¡Pasajero eliminado!")

    return redirect('/pasajeros')




#Registrarse como usuario
def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            #redirigir al home
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request,"Te has registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario

    return render(request,'registration/registro.html',data)
