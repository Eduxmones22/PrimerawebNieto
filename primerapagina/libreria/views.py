from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from .forms import *
import datetime, random 


# Create your views here.
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
            return render(request, "libreria/listar_escritores.html", {"profesores": escritores})
    else:
        form = EscritorForm()
    return render(request, 'libreria/crear_escritor.html', {'form': form})

def Escritores(request):
    escritores = Escritor.objects.all()
    return render(request, "libreria/listar_escritores.html", {"profesores": escritores})


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
        form = EscritorForm()
    return render(request, 'libreria/crear_escritor.html', {'form': form})

def Libros(request):
    libros = Libro.objects.all()
    return render(request, "libreria/listar_escritores.html", {"libros": libros})









def crear_libro(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'crear_libro.html', {'form': form})

def crear_comentario(request):
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_comentarios')
    else:
        form = ComentarioForm()
    return render(request, 'crear_comentario.html', {'form': form})
