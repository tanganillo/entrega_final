from django.urls import path
from . import views
from .views import PaginaCreateView, PaginaUpdateView, PaginaDeleteView, AboutView

urlpatterns = [
    # ejemplo de ruta, aunque sea vacía para iniciar
    path('', views.home, name='home'),
    path('pages/create/', PaginaCreateView.as_view(), name='pagina-create'),
    path('pages/<int:pk>/edit/', PaginaUpdateView.as_view(), name='pagina-update'),
    path('pages/<int:pk>/delete/', PaginaDeleteView.as_view(), name='pagina-delete'),
    path('about/', AboutView.as_view(), name='about'),
]

