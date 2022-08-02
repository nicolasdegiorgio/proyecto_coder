from django.db import models

# Create your models here.


class Curso(models.Model):
    
    nombre= models.CharField(max_length=40)
    camada=models.IntegerField()
    
    def __str__(self) -> str:
        return f"{self.nombre} - Camada: {self.camada}"
    
class Estudiante(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email = models.EmailField()   #Es un campo que solo acepta caracteres de email
    
    
class Profesor(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email = models.EmailField()
    profesion= models.CharField(max_length=30)
    
    
class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()
