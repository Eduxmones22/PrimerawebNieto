from django import forms
from .models import Escritor, Libro, Comentario

class EscritorForm(forms.ModelForm):
    class Meta:
        model = Escritor
        fields = ['nombre', 'nacionalidad', 'fecha_nacimiento']

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'genero', 'fecha_publicacion', 'escritor']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['libro', 'usuario', 'contenido']
