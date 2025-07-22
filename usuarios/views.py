#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegistroForm
from .models import Perfil
from .forms import EditarPerfilForm
from django.contrib import messages
from django.contrib.auth import logout
from django.views.decorators.http import require_POST

def profile(request):
    return render(request, 'usuarios/profile.html')


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            perfil, creado = Perfil.objects.get_or_create(user=user)
            perfil.nombre = form.cleaned_data.get('first_name')
            perfil.apellido = form.cleaned_data.get('last_name')
            perfil.avatar = form.cleaned_data.get('avatar')
            perfil.email = form.cleaned_data.get('email')
            perfil.save()
            messages.success(request, "✅ Tu cuenta fue creada con éxito. ¡Bienvenido al blog musical!")
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})

@login_required
def perfil(request):
    return render(request, 'usuarios/perfil.html', {
        'perfil': request.user.perfil
    })

@login_required
def editar_perfil(request):
    perfil = request.user.perfil
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Perfil actualizado correctamente.")
            return redirect('profile')
    else:
        form = EditarPerfilForm(instance=perfil)
    return render(request, 'usuarios/editar_perfil.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    messages.info(request, "👋 Cerraste sesión exitosamente. ¡Te esperamos pronto!")
    return redirect('login')

@login_required
@require_POST
def eliminar_perfil(request):
    perfil = request.user.perfil
    perfil.delete()
    logout(request)
    messages.success(request, "🗑️ Perfil eliminado. Cerraste sesión automáticamente.")
    return redirect('home')


@login_required
def listar_perfiles(request):
    perfiles = Perfil.objects.select_related('user').all()
    return render(request, 'usuarios/listar_perfiles.html', {'perfiles': perfiles})