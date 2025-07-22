from django.db import models
from django.contrib.auth.models import User
    

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='noticias/', null=True, blank=True)
    fecha = models.DateField(auto_now_add=True, editable=False)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    genero = models.CharField(max_length=100, default="General", choices=[
        ('rock', 'Rock'),
        ('pop', 'Pop'),
        ('trap', 'Trap'),
        ('reggaeton', 'Reggaetón'),
        ('electronica', 'Electrónica'),
        ('indie', 'Indie'),
        ('reggae', 'Reggae'),
        ('hip-hop', 'Hip Hop'),
    ])
    etiquetas = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.titulo