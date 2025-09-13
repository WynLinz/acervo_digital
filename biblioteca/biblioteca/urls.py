from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', admin.site.urls), # utilize o apóstrofo ('') vazio para link direto
]