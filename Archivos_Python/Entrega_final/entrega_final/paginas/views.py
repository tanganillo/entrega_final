from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Pagina
from django.views.generic import TemplateView
from django.shortcuts import render

class PaginaCreateView(LoginRequiredMixin, CreateView):
    model = Pagina
    fields = ['titulo', 'subtitulo', 'imagen', 'contenido']
    template_name = 'paginas/pagina_form.html'
    success_url = '/pages/'

class PaginaUpdateView(LoginRequiredMixin, UpdateView):
    model = Pagina
    fields = ['titulo', 'subtitulo', 'imagen', 'contenido']
    template_name = 'paginas/pagina_form.html'
    success_url = '/pages/'

class PaginaDeleteView(LoginRequiredMixin, DeleteView):
    model = Pagina
    template_name = 'paginas/pagina_confirm_delete.html'
    success_url = '/pages/'

class AboutView(TemplateView):
    template_name = 'paginas/sobre_mi.html'

def home(request):
    ultimas = Pagina.objects.order_by('-pub_date')[:3]  # Muestra las 3 últimas noticias
    return render(request, 'paginas/home.html', {'ultimas': ultimas})
