from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Perfil

@receiver(post_save, sender=User)
def crear_o_guardar_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)
    elif hasattr(instance, 'perfil'):
        try:
            instance.perfil.save()
        except Exception:
            pass  # o logueás el error si querés hacer debug
