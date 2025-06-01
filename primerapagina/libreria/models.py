from django.db import models

# Create your models here.
class Escritor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    escritor = models.ForeignKey(Escritor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} - {self.libro.titulo}"
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    curso = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} - {self.curso}"

class Prestamo(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_retiro = models.DateField()
    fecha_devolucion = models.DateField()

    def __str__(self):
        return f"{self.estudiante.nombre} - {self.libro.nombre} ({self.fecha_retiro} → {self.fecha_devolucion})"

    
