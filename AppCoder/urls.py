from AppCoder.views import * 
from django.urls import path


urlpatterns = [
    path('', home),
    path('cursos/', cursos),
    path('entregables/', entregables),
    path('estudiantes/', estudiantes),
    path('profesores/', profesores),
    path('api_estudiantes/', api_estudiantes),
    path('buscar_estudiantes/', buscar_estudiantes),
    path('create_estudiantes/', create_estudiantes),    
    path('read_estudiantes/', read_estudiantes),    
    path('update_estudiantes/<estudiante_id>', update_estudiantes),    
    path('delete_estudiantes/<estudiante_id>', delete_estudiantes),    

]