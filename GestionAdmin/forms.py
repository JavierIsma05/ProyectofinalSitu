from dataclasses import fields
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class ViajeForm(forms.ModelForm):
    class Meta:
        model = Viaje
        fields = '__all__'

class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = '__all__'


class TarjetaForm(forms.ModelForm):
    class Meta:
        model = Tarjeta
        fields = '__all__'
        
class PasajeroForm(forms.ModelForm):
    class Meta:
        model = Pasajero
        fields = '__all__'

class SimuladorForm(forms.ModelForm):
    class Meta:
        model = AccesoPago
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    pass