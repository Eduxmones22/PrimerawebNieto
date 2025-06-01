"""
URL configuration for primerapagina project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from libreria.views import crear_escritor, crear_libro, crear_estudiante, index, Escritores, Libros, Estudiantes, buscar_libro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),  # Esto carga 'index.html' al iniciar el servidor
    path('crear_escritor/', crear_escritor, name='crear_escritor'),
    path('listar_escritores/', Escritores, name='listar_escritores'),
    path('crear_libro/', crear_libro, name='crear_libro'),
    path('listar_libros/', Libros, name='listar_libros'),
    path('crear_estudiante/', crear_estudiante, name='crear_estudiante'),
    path('listar_estudiantes/', Estudiantes, name='listar_estudiantes'),
    path('buscar-libro/', buscar_libro, name='buscar_libro'),    
]

