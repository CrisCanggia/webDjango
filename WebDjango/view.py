from xml.dom.minidom import Document
from django.http import HttpResponse
from django.template import loader
from AppCoder.models import Curso

def home(self,name):
    return HttpResponse(f'Hola soy {name}')

def homePage(self):
    lista = [1,2,3,4,5,6,7,8,9]
    data = {'nombre':'Cristian', 'apellido':'Canggianelli', 'lista':lista}
    planilla = loader.get_template('home.html')     # aqui llamo mediante el loader el tmplate en html. Loader debe estar definido en settings / templates
    documento = planilla.render(data)               # Indicar la variable del diccionario
    return HttpResponse(documento)

def cursos(self):
    #planilla = loader.get_template('cursos.html')
    curso = Curso(nombre="UX/UI", camada="12345")
    curso.save()
    documento = f'Curso: {curso.nombre} camada: {curso.camada}' 
    return HttpResponse(documento)

