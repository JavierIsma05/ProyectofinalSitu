from django.db import models
from django.contrib.auth.models import User


class TarjetaTransporte(models.Model):
    codigo_tarjeta = models.CharField(max_length=20, unique=True)
    clave_tarjeta = models.CharField(max_length=50)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.codigo_tarjeta) 
    
    class Meta:
        verbose_name = 'TarjetaTransporte'
        verbose_name_plural = 'TarjetaTransportes'

class Pasajero(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=10)
    tarjeta_transporte = models.OneToOneField(TarjetaTransporte, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombre) 
    
    class Meta:
        verbose_name = 'Pasajero'
        verbose_name_plural = 'Pasajeros'

class Administrador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Puedes agregar más campos para información adicional del administrador si es necesario

class Bus(models.Model):
    placa = models.CharField(max_length=15, unique=True)
    modelo = models.CharField(max_length=50)
    capacidad_pasajeros = models.IntegerField()
    pasajeros = models.ManyToManyField(Pasajero, through='Viaje')  # Relación muchos a muchos con Pasajero a través de Viaje
    
    def __str__(self):
        return str(self.placa) 
    
    class Meta:
        verbose_name = 'Bus'
        verbose_name_plural = 'Buses'


class Viaje(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    pasajero = models.ForeignKey(Pasajero, on_delete=models.CASCADE)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    costo_tarifa = models.DecimalField(max_digits=10, decimal_places=2)
    # Otros campos relacionados con el viaje, como la duración, la hora de salida, etc.
    def __str__(self):
        return str(self.bus) 
    class Meta:
        verbose_name = 'Viaje'
        verbose_name_plural = 'Viajes'
