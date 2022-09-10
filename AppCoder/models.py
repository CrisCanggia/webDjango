from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=40)                #Formato str con max de carcateres
    camada = models.IntegerField()                          #Formato numerico

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)                #Formato str con max de carcateres
    apellido = models.CharField(max_length=30)              #Formato str con max de carcateres
    email = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)                #Formato str con max de carcateres
    apellido = models.CharField(max_length=30)              #Formato str con max de carcateres
    email = models.EmailField()                             #Formato Email (@ y .com)
    profesion = models.CharField(max_length=30)             #Formato str con max de carcateres

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)                #Formato str con max de carcateres
    fechaDeEntrega = models.DateField()                     #Formato Fecha
    entregada = models.BooleanField()                       #true or False.
    
