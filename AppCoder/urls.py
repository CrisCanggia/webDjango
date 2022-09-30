from AppCoder.views import * 
from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static




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
    path('login/', login_request),
    path('registro/', registro),
    path('logout/', LogoutView.as_view(template_name = 'inicio.html'), name="logout"),
    path('perfil/', perfilView),
    path('perfil/editarPerfil/', editarPerfil),
    path('perfil/changepass/', changepass),
    path('perfil/changeAvatar/', AgregarAvatar),



]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
