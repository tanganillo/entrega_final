from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatares/', default='avatares/default.png')
    email = models.EmailField(max_length=254, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} - Perfil'

@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)
