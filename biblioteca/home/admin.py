# Remover superuser
# > python manage.py shell
#$ from django.contrib.auth.models import User
#$ User.objects.get(username="test", is_superuser=True).delete()

from django.contrib import admin, messages
from django.shortcuts import redirect, get_object_or_404
from django.urls import path
from .models import Livro
from .models import Aluno
from .models import Revista
import subprocess

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('Autor', 'Titulo', 'Prateleira', 'Em_uso') # principais subcategorias que serão exibidas
    search_fields = ('Autor', 'Titulo', 'Prateleira', 'Em_uso')

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('Nome', 'Sala', 'Serie', 'Livro_em_posse', 'Data_coleta','Data_devolução')
    search_fields = ('Nome', 'Sala', 'Serie', 'Livro_em_posse')

@admin.register(Revista)
class RevistaAdmin(admin.ModelAdmin):
    list_display = ('Autor', 'Titulo', 'Prateleira', 'Em_uso')
    search_fields = ('Autor', 'Titulo', 'Prateleira', 'Em_uso')