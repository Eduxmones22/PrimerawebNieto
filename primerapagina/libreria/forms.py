from django import forms
from .models import Escritor, Libro, Estudiante, Prestamo

class EscritorForm(forms.ModelForm):
    class Meta:
        model = Escritor
        fields = ['nombre', 'nacionalidad', 'fecha_nacimiento']

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'genero', 'fecha_publicacion', 'escritor']
        
class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'curso', 'email']      

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['estudiante', 'libro', 'fecha_retiro', 'fecha_devolucion']
        widgets = {
            'fecha_retiro': forms.DateInput(attrs={'type': 'date'}),
            'fecha_devolucion': forms.DateInput(attrs={'type': 'date'}),
        }
