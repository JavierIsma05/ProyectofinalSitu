'''
from django.shortcuts import render
from rest_framework import generics
from api.models import Item
from api.serializers import ItemSerializer

class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item
    serializer_class = ItemSerializer

'''
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

# --------------------------------------------------CREACION DE API------------------------------------------------------


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'list': '/item-list',
        'Detail View': '/item-detail/<str:pk>',
        'Create': '/item-create/',
        'Update': '/item-update/<str:pk>',
        'Delete': '/item-delete/<str:pk>',
    }
    return Response(api_urls)

# Metodo GET Trae todos los items


@api_view(['GET'])
def itemList(resquest):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


# Metodo GET me trae por id
@api_view(['GET'])
def itemDetail(resquest, pk):
    items = Item.objects.get(id=pk)
    serializer = ItemSerializer(items, many=False)
    return Response(serializer.data)


# Metodo POST
@api_view(['POST'])
def itemCreate(resquest):
    serializer = ItemSerializer(data=resquest.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print('Dato incorrecto')
    return Response(serializer.data)


# Metodo UPDATE por id
@api_view(['PUT'])
def itemUpdate(resquest, pk):
    item = Item.objects.get(id=pk)
    serializer = ItemSerializer(instance=item, data=resquest.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print('Dato incorrecto')
    return Response(serializer.data)


# Metodo DELETE por id
@api_view(['DELETE'])
def itemDelete(resquest, pk):
    item = Item.objects.get(id=pk)
    item.delete()
    return Response('Item Eliminada.............')
