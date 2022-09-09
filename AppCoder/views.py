from django.shortcuts import render 
from xml.dom.minidom import Document
from django.http import HttpResponse
from django.template import loader
from AppCoder.models import Curso
from django.http import HttpResponse

def inicio(request):
    return render(request, "inicio.html")

def cursos(request):
    return render(request, "cursos.html")

def profesores(request):
    return render(request, "profesores.html")

def estudiantes(request):
    return render(request, "estudiantes.html")

def entregables(request):
    return render(request, "entregables.html")


