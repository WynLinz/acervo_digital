from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', admin.site.urls), # Deixe o path como admin, utilizar apóstrofo vazio sempre irá chamar outros paths como admin
]