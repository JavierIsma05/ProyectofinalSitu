from dataclasses import fields
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
        model = TarjetaTransporte
        fields = '__all__'
        
class PasajeroForm(forms.ModelForm):
    class Meta:
        model = Pasajero
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',"first_name","last_name","email","password1","password2"]