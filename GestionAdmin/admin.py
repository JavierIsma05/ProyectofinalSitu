from django.contrib import admin
from .models import *

class ViajeModel(admin.ModelAdmin): 
    list_display = ["bus","pasajero","fecha_ingreso","costo_tarifa"]
class TarjetaTransporteModel(admin.ModelAdmin):
    list_display = ["codigo_tarjeta","clave_tarjeta","saldo"]

class PasajeroModel(admin.ModelAdmin):
    list_display = ["nombre","tarjeta_transporte"]

class BusModel(admin.ModelAdmin):
    list_display = ["placa","modelo","capacidad_pasajeros"]

admin.site.register(Viaje,ViajeModel)
admin.site.register(Bus,BusModel)    
admin.site.register(TarjetaTransporte,TarjetaTransporteModel)
admin.site.register(Pasajero,PasajeroModel)
