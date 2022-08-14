from django.shortcuts import render
from .forms import ViajeForm,BusForm,TarjetaForm,PasajeroForm,SimuladorForm,CustomUserCreationForm
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.

def home_view(request):
    return render(request,"app/home.html",{})

def about_view(request):
    return render(request,"app/about.html",{})

def contact_view(request):
    return render(request,"app/contact.html",{})

#formularios
def agregar_pasajero(request):
    data = { 
        'form':PasajeroForm()
    }

    if request.method == 'POST':
        formulario = PasajeroForm(data=request.POST,files = request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Información guardada"
        else:
            data["form"] = formulario
    return render(request, 'app/pasajero/agregar.html',data)

def agregar_bus(request):
    data = { 
        'form':BusForm()
    }

    if request.method == 'POST':
        formulario = BusForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Información guardada"
        else:
            data["form"] = formulario
    return render(request, 'app/buses/agregar.html',data)

#poner tablas

def Tarjeta_list(request):
    tarjeta = Tarjeta.objects.all()
    contexto = {'tarjetas':tarjeta}
    return render(request,'tarjeta_lista.html',contexto)

def pasajero_view(request):
    pasajero = Pasajero.objects.all()
    context = {'pasajeros':pasajero}
    return render(request,"app/pasajero/listar.html",context)

def buses_view(request):
    bus = Bus.objects.all()
    context = {'buses':bus}
    return render(request,"app/buses/listar.html",context)

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
            #return redirect(to="home")
        data["form"] = formulario

    return render(request,'registration/registro.html',data)