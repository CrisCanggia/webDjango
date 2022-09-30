from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=40)                #Formato str con max de carcateres
    camada = models.IntegerField()                          #Formato numerico
    
    
    def __str__(self):
        return f"Nombre:{self.nombre} - Camada:{self.camada}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)                #Formato str con max de carcateres
    apellido = models.CharField(max_length=30)              #Formato str con max de carcateres
    email = models.EmailField()

    def __str__(self):
        return f"Nombre:{self.nombre} - Apellido:{self.apellido} - Email:{self.email}"    #El metodo sirve para que dentro del Admin se vea la infor mejor.

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)                #Formato str con max de carcateres
    apellido = models.CharField(max_length=30)              #Formato str con max de carcateres
    email = models.EmailField()                             #Formato Email (@ y .com)
    profesion = models.CharField(max_length=30)             #Formato str con max de carcateres



class Entregable(models.Model):
    nombre = models.CharField(max_length=30)                #Formato str con max de carcateres
    fechaDeEntrega = models.DateField()                     #Formato Fecha
    entregada = models.BooleanField()                       #true or False.
    
class Avatar(models.Model):
    #vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #subcarpeta Avatares de media
    image = models.ImageField(upload_to='avatares', null = True, blank = True)
