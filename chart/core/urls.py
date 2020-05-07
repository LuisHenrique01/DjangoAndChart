from django.contrib import admin
from django.urls import path
from .views import index, importar

urlpatterns = [
    path('', index, name='index'),
    path('importa/', importar, name='importar')
]