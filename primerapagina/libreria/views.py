from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from .forms import *
import datetime, random 


# Create your views here.
def index(request):
    return render(request, 'libreria/index.html')

def crear_escritor(request):
    if request.method == "POST":
        form = EscritorForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            nacionalidad = form.cleaned_data["nacionalidad"]
            fecha_nacimiento = form.cleaned_data["fecha_nacimiento"]
            escritor = Escritor(nombre=nombre, nacionalidad=nacionalidad, fecha_nacimiento=fecha_nacimiento)
            escritor.save()
            escritores = Escritor.objects.all()
            return render(request, "libreria/listar_escritores.html", {"escritores": escritores})
    else:
        form = EscritorForm()
    return render(request, 'libreria/crear_escritor.html', {'form': form})

def Escritores(request):
    escritores = Escritor.objects.all()
    return render(request, "libreria/listar_escritores.html", {"escritores": escritores})


def crear_libro(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data["titulo"]
            genero = form.cleaned_data["genero"]
            fecha_publicacion = form.cleaned_data["fecha_publicacion"]
            escritor = form.cleaned_data["escritor"]
            escritor = Libro(titulo=titulo, genero=genero, fecha_publicacion=fecha_publicacion,escritor=escritor)
            escritor.save()
            libros = Libro.objects.all()
            return render(request, "libreria/listar_libros.html", {"libros": libros})
    else:
        form = LibroForm()
    return render(request, 'libreria/crear_libro.html', {'form': form})

# def Libros(request):
#     libros = Libro.objects.all()
#     return render(request, "libreria/listar_libros.html", {"libros": libros})

def Libros(request):
    query = request.GET.get('q', '')  # Obtiene el término de búsqueda
    if query:
        libros = Libro.objects.filter(titulo__icontains=query)  # Filtra por título
    else:
        libros = Libro.objects.all()  # Si no hay búsqueda, muestra todos

    return render(request, 'libreria/listar_libros.html', {'libros': libros, 'query': query})

def crear_estudiante(request):
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            curso = form.cleaned_data["curso"]
            email = form.cleaned_data["email"]
            estudiante = Estudiante(nombre=nombre, curso=curso, email=email)
            estudiante.save()
            estudiantes = Estudiante.objects.all()
            return render(request, "libreria/listar_estudiantes.html", {"estudiante": estudiantes})
    else:
        form = EstudianteForm()
    return render(request, 'libreria/crear_estudiante.html', {'form': form})

def Estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, "libreria/listar_estudiantes.html", {"estudiante": estudiantes})

def buscar_libro(request):
    query = request.GET.get('q')  # Obtiene el término de búsqueda
    libros = Libro.objects.filter(nombre__icontains=query) if query else []
    return render(request, 'buscar_libro.html', {'libros': libros, 'query': query})
