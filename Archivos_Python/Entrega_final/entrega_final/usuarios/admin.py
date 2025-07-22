from django.contrib import admin
from django.contrib.auth.models import User
from usuarios.models import Perfil

for user in User.objects.all():
    Perfil.objects.get_or_create(user=user)