from django.urls import path
from . import views
from .views import (
    NoticiaCreateView, NoticiaUpdateView, NoticiaDeleteView,
    NoticiaListView, NoticiaDetailView, AboutView, home
)

urlpatterns = [
    # ejemplo de ruta, aunque sea vacía para iniciar
    path('', views.home, name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('noticias/', NoticiaListView.as_view(), name='lista-noticias'),
    path('noticias/nueva/', NoticiaCreateView.as_view(), name='crear-noticia'),
    path('noticias/<int:pk>/', NoticiaDetailView.as_view(), name='detalle-noticia'),
    path('noticias/<int:pk>/editar/', NoticiaUpdateView.as_view(), name='editar-noticia'),
    path('noticias/<int:pk>/eliminar/', NoticiaDeleteView.as_view(), name='eliminar-noticia'),
]

