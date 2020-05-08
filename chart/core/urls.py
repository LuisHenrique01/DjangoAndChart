from django.contrib import admin
from django.urls import path
from .views import index, importar, home

urlpatterns = [
    path('', index, name='index'),
    path('importa/', importar, name='importar'), 
    path('home/', home, name='home')
]