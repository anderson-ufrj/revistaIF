from django.db import models

# Create your models here.
class Tipo(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    

class Curso(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Periodo(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=500)
    curso  = models.ForeignKey(Curso, on_delete= models.CASCADE)
    periodo  = models.ForeignKey(Periodo, on_delete= models.CASCADE)
    tipousuario = models.ForeignKey(Tipo, on_delete= models.CASCADE)

    def __str__(self):
        return self.nome

    
class TipoArtigo(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Artigo(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100, blank=True)
    resumo = models.CharField(max_length=500)
    conteudo  = models.CharField(max_length=10000)
    autor = models.ForeignKey(Usuario, on_delete= models.CASCADE)
    tipoartg = models.ForeignKey(TipoArtigo, on_delete= models.CASCADE)


    def __str__(self):
        return self.titulo