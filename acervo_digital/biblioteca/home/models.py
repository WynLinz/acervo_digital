from django.db import models

class Livro(models.Model):
    Autor = models.CharField(max_length=100, verbose_name='Autor:')
    Titulo = models.CharField(max_length=100, verbose_name='Título:')
    Em_uso = models.BooleanField(default=False, verbose_name='Em uso:')
    Subtitulo = models.CharField(max_length=100, blank=True, null=True, default=None, verbose_name='Subtítulo:')
    Colecao = models.CharField(max_length=100, blank=True, null=True, default=None, verbose_name='Coleção:')
    Serie = models.CharField(max_length=100, blank=True, null=True, default=None, verbose_name='Série:')
    Edicao = models.CharField(max_length=100, blank=True, null=True, default=None, verbose_name='Edição:')
    Volume = models.IntegerField(null=True, blank=True, default=None, verbose_name='Volume:')
    Local = models.CharField(max_length=100, blank=True, null=True, default=None, verbose_name='Local:')
    Editora = models.CharField(max_length=100, blank=True, null=True, default=None, verbose_name='Editora:')
    Ano_Publicacao = models.DateField(null=True, blank=True, default=None, verbose_name='Ano de Publicação:')
    Aquisicao = models.CharField(max_length=100, blank=True, null=True, default=None, verbose_name='Aquisição:')
    Exemplar = models.IntegerField(null=True, blank=True, default=None, verbose_name='Exemplar:')
    Idioma = models.CharField(null=True, blank=True, max_length=100, default=None, verbose_name='Idioma:')
    Paginas = models.IntegerField(null=True, blank=True, default=None, verbose_name='Páginas:')
    Tombo = models.IntegerField(null=True, blank=True, default=None, verbose_name='Tombo:')
    Data_Tombo = models.DateField(null=True, blank=True, default=None, verbose_name='Data Tombo:')
    Data_Registro = models.DateField(null=True, blank=True, default=None, verbose_name='Data de Registro:')
    ISBN = models.IntegerField(null=True, blank=True, default=None, verbose_name='ISBN:')
    Cod_Barras = models.IntegerField(null=True, blank=True, default=None, verbose_name='Código de barras:')
    Data_Baixa = models.DateField(null=True, blank=True, default=None, verbose_name='Data de baixa:')
    Observacao = models.TextField(null=True, blank=True, default=None, verbose_name='Observação:')
    Classif_CDD = models.IntegerField(null=True, blank=True, default=None, verbose_name='Classificação CDD:')
    Assunto = models.TextField(null=True, blank=True, default=None, verbose_name='Assunto:')
    Prateleira = models.CharField(max_length=100, verbose_name='Prateleira:')

class Revista(models.Model):
    Autor = models.CharField(max_length=100, verbose_name='Autor:')
    Titulo = models.CharField(max_length=100, verbose_name='Título:')
    Em_uso = models.BooleanField(default=False, verbose_name='Em uso:')
    Subtitulo = models.CharField(max_length=100, blank=True, null=True, default=None, verbose_name='Subtítulo:')
    Colecao = models.CharField(max_length=100, blank=True, null=True, default=None, verbose_name='Coleção:')
    Local = models.CharField(max_length=100, blank=True, null=True, default=None, verbose_name='Local:')
    Idioma = models.CharField(null=True, blank=True, max_length=100, default=None, verbose_name='Idioma:')
    Ano_Publicacao = models.DateField(null=True, blank=True, default=None, verbose_name='Ano de Publicação:')
    Aquisicao = models.CharField(max_length=100, blank=True, null=True, default=None, verbose_name='Aquisição:')
    Exemplar = models.IntegerField(null=True, blank=True, default=None, verbose_name='Exemplar:')
    Tombo = models.IntegerField(null=True, blank=True, default=None, verbose_name='Tombo:')
    Data_Tombo = models.DateField(null=True, blank=True, default=None, verbose_name='Data Tombo:')
    Data_Registro = models.DateField(null=True, blank=True, default=None, verbose_name='Data de Registro:')
    ISBN = models.IntegerField(null=True, blank=True, default=None, verbose_name='ISBN:')
    Numero = models.IntegerField(null=True, blank=True, default=None, verbose_name='Número:')
    Cod_Barras = models.IntegerField(null=True, blank=True, default=None, verbose_name='Código de barras:')
    Data_Baixa = models.DateField(null=True, blank=True, default=None, verbose_name='Data de baixa:')
    Observacao = models.TextField(null=True, blank=True, default=None, verbose_name='Observação:')
    Prateleira = models.CharField(max_length=100, verbose_name='Prateleira:')

class Aluno(models.Model):
      Nome = models.CharField(max_length=50, verbose_name='Nome:')
      RA = models.CharField(max_length=50, blank=True, null=True, verbose_name='RA:')
      Sala = models.CharField(max_length=50, verbose_name='Sala:')
      Serie = models.CharField(max_length=5, verbose_name='Série:')
      Livro_em_posse = models.CharField(max_length=256, blank=True, verbose_name='Livro em posse:')
      Data_coleta = models.DateField(null=True, blank=True, verbose_name='Data de coleta:')
      Data_devolução = models.DateField(null=True, blank=True, verbose_name='Data de Devolução:')
      Observacao = models.TextField(null=True, blank=True, verbose_name='Observação:')

def __str__(self):
        return self.nome

# Create your models here.



# IMPORTAR LIVROS NO MYSQL