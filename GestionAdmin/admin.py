from django.contrib import admin
from .models import *


class PasajeroModel(admin.ModelAdmin):
    list_display = ["nombre","apellido","email","edad","sexo"]
    list_filter = ["edad","sexo"]
    search_fields = ["apellido"]
    list_per_page = 5
class TarjetaModel(admin.ModelAdmin):
    list_editable = ["monto"]
    list_display = ["codigo","monto","idPasajero"]

class BusModel(admin.ModelAdmin):
    list_display = ["placa","capacidad","cooperativa","tipo"]
     
class ViajeModel(admin.ModelAdmin):
    list_display = ["bus","costo","fecha_viaje","efectivo"]
    search_fields = ["costo"]

class SimularModel(admin.ModelAdmin):
    list_display = ["numero","fecha_viaje"]

admin.site.register(Profile)
admin.site.register(Viaje,ViajeModel)
admin.site.register(Bus,BusModel)    
admin.site.register(Tarjeta,TarjetaModel)
admin.site.register(Pasajero,PasajeroModel)
admin.site.register(AccesoPago,SimularModel)
