from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from usuarios.views import eliminar_perfil, listar_perfiles

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('usuarios/login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('perfil/', views.perfil, name='profile'),
    path('perfil/editar/', views.editar_perfil, name='editar-perfil'),
    #path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('perfil/eliminar/', eliminar_perfil, name='eliminar-perfil'),
    path('perfiles/', listar_perfiles, name='listar-perfiles'),
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='usuarios/cambiar_contraseña.html',
        success_url='/usuarios/perfil/'
    ), name='password_change'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)