from operator import mod
from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.EmailField()

class Tag(models.Model):
    name = models.CharField(max_length=40)

class Post(models.Model):
    titulo = models.CharField(max_length=40)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    fecha_edicion = models.DateTimeField(auto_now=True) 
    tags = models.ManyToManyField(Tag)
    #imagen = models.ImageField()
    #autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    #autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    contenido = models.TextField()
    post=models.ForeignKey(Post, on_delete=models.CASCADE)

class Like(models.Model):
    #usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # def __str__(self):
    #     return self.usuario



