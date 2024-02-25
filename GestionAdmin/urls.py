from django.urls import path
from .views import *

urlpatterns = [
	
	path('', home_view, name= 'home'),
	path('about/', about_view, name = 'about'),
    
	#BUSES
    path('buses/', buses, name='buses'),
    path('registrarBus/', registrarBus, name='registrarBus'),
    path('edicionBus/<placa>', edicionBus, name='edicionBus'),
    path('eliminarBus/<placa>', eliminarBus, name='eliminarDocente'),
    path('editarBus/', editarBus, name='editarBus'),
	
	#PASAJEROS
	path('pasajeros/',pasajeros,name='pasajeros'),
	path('registrarPasajero/',registrarPasajero,name='registrarPasajero'),
	path('edicionPasajero/<codigo>',edicionPasajero,name='edicionPasajero'),
	path('editarPasajero/<codigo>/',editarPasajero,name='editarPasajero'),
    

	path('registro/',registro,name='registro'),
	

]