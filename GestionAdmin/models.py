from bdb import effective
from statistics import mode
from tabnanny import verbose
from django.db import models
from .choices import *
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    
    #IMAGEN
    def __str__(self):
        return f'Perfil de {self.user.username}'

class Pasajero(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(verbose_name='Correo')
    edad = models.PositiveIntegerField()
    sexo = models.CharField(max_length=1,verbose_name='Genero',choices=sexos, default='F')
    
    def __str__(self) :
        return '{}'.format(self.nombre)
    class Meta:
        verbose_name = 'Pasajero'
        verbose_name_plural = 'Pasajeros'
        
class Tarjeta(models.Model):
    codigo = models.CharField(max_length=6,blank=False)
    monto = models.CharField(max_length=30)
    idPasajero = models.ForeignKey(Pasajero,on_delete=models.CASCADE)
    
    def __str__(self) :
        return f'Tarjeta: {self.codigo} | Pasajero: {str(self.idPasajero)} | Monto Tarjeta: {str(self.monto)}'
    class Meta:
        verbose_name = 'Tarjeta'
        verbose_name_plural = 'Tarjetas'
        
class Bus(models.Model):
    placa = models.CharField(max_length=50)
    capacidad = models.IntegerField()
    cooperativa = models.CharField(max_length=30)
    tipo = models.CharField(max_length=1,verbose_name='Tipo',choices=tipo, default='F')
    idTarjeta = models.ManyToManyField(Pasajero)
    
    def __str__(self) :
        return '{}'.format(self.placa)
    class Meta:
        verbose_name = 'Bus'
        verbose_name_plural = 'Buses'
            

class Viaje(models.Model):
    pasajero = models.ForeignKey(Pasajero,on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus,on_delete=models.CASCADE)
    costo = models.DecimalField(max_digits=4,decimal_places=2)
    cantidad = models.IntegerField()
    fecha_viaje = models.DateTimeField(auto_now_add=True)
    efectivo = models.BooleanField(default=True)
    tipo = models.CharField(max_length=20,choices=confortViaje, default='F')
    
    def __str__(self) :
        return f'Pasj.Nombre: {self.pasajero.nombre} | Precio: {str(self.costo)}'
    class Meta:
        verbose_name = 'Viaje'
        verbose_name_plural = 'Viajes'
    
class AccesoPago(models.Model):
    numero= models.CharField(max_length=7,blank=False)
    fecha_viaje = models.DateTimeField(auto_now_add=True)
    viaje = models.ForeignKey(Viaje,on_delete=models.CASCADE)
    tarjeta = models.ForeignKey(Tarjeta,on_delete=models.CASCADE)
    
    def __str__(self) :
        return f'Pasajero: {self.viaje.pasajero.nombre}'
    
    class Meta:
        verbose_name = 'AccesoPago'
        verbose_name = 'AccesoPagos'