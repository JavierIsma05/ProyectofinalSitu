from django.urls import path
from .views import *

urlpatterns = [
	path('', home_view, name= 'home'),
	path('pasajero/',pasajero_view, name='pasajero'),
	path('bus/',buses_view, name='bus'),
	
	path('about/', about_view, name = 'about'),
	path('agregar-pasajero/', agregar_pasajero, name = 'agregar_pasajero'),
	path('agregar-bus/',agregar_bus, name='agregar_bus'),
	path('contact/',contact_view,name='contact'),
	path('registro/',registro,name='registro'),

]