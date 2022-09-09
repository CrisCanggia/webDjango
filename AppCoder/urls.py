from AppCoder.views import * 
from django.urls import path


urlpatterns = [
    path('', inicio),
    path('cursos/', cursos),
    path('entregables/', entregables),
    path('estudiantes/', estudiantes),
    path('profesores/', profesores),
]