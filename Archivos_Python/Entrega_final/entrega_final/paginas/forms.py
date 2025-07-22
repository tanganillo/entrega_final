from django import forms
from .models import Noticia

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        exclude = ['fecha']  # 🔒 no se edita
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '🎤 Título de la noticia'
            }),
            'contenido': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '📝 Escribí el contenido completo'
            }),
            'imagen': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'genero': forms.Select(attrs={
                'class': 'form-select'
            }),
            'etiquetas': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '🎶 Etiquetas separadas por coma'
            }),
        }
