from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Noticia
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render
from django.db.models import Q
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import NoticiaForm


def home(request):
    todas = Noticia.objects.order_by('-id')
    ultimas = todas[:4]
    anteriores = todas[4:10]  # desde la 5ta a la décima

    return render(request, 'paginas/home.html', {
        'ultimas': ultimas,
        'anteriores': anteriores,
    })

class AboutView(TemplateView):
     template_name = 'paginas/sobre_mi.html'

class NoticiaCreateView(LoginRequiredMixin, CreateView):
    model = Noticia
    fields = ['titulo', 'contenido', 'imagen','genero', 'etiquetas']  # no incluyas 'autor'
    template_name = 'paginas/noticia_crear.html'
    success_url = '/noticias/'

    def form_valid(self, form):
        form.instance.autor = self.request.user  # ⬅️ Asigna el autor logueado
        return super().form_valid(form)

class NoticiaUpdateView(LoginRequiredMixin, UpdateView):
    model = Noticia
    fields = ['titulo', 'contenido', 'imagen','genero', 'etiquetas']
    template_name = 'paginas/noticia_crear.html'
    success_url = '/noticias/'

class NoticiaDeleteView(LoginRequiredMixin, DeleteView):
    model = Noticia
    template_name = 'paginas/noticia_eliminar.html'
    success_url = reverse_lazy('lista-noticias')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "🧹 Noticia eliminada con éxito.")
        return super().delete(request, *args, **kwargs)

class NoticiaListView(ListView):
    model = Noticia
    template_name = 'paginas/noticia_lista.html'
    context_object_name = 'noticias'
    ordering = ['-id']
    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(titulo__icontains=q) | Q(contenido__icontains=q)
            )
        return queryset

class NoticiaDetailView(DetailView):
    model = Noticia
    template_name = 'paginas/noticia_detalle.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        noticia = self.object

        if noticia.fecha:
            context['anterior'] = Noticia.objects.filter(fecha__lt=noticia.fecha).order_by('-fecha').first()
            context['siguiente'] = Noticia.objects.filter(fecha__gt=noticia.fecha).order_by('fecha').first()
        else:
            context['anterior'] = None
            context['siguiente'] = None

        return context


