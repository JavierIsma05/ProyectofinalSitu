'''
from django.urls import path
from api.views import ItemList,ItemDetail  
urlpatterns = [
    path('api/items',ItemList.as_view()),
    path('api/items/<int:pk>',ItemDetail.as_view()),
]
'''
from .import views
from django.urls import path

urlpatterns = [
    path('', views.apiOverview, name="apiOverview"),
    path('item-list', views.itemList, name="item-list"),
    path('item-detail/<str:pk>', views.itemDetail, name="item-detail"),
    path('item-create', views.itemCreate, name="item-create"),
    path('item-update/<str:pk>', views.itemUpdate, name="item-update"),
    path('item-delete/<str:pk>', views.itemDelete, name="item-delete"),
]