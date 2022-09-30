import email
from django.shortcuts import render, redirect 
from AppCoder.models import Estudiante, Curso, Avatar
from django.http import HttpResponse
from AppCoder.forms import UserRegisterForm, form_estudiantes, UserEditForm, ChangePasswordForm, AvatarFormulario

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 

def inicio(request):
    return render(request, "inicio.html")
@login_required
def home(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None           
    return render(request, 'home.html', {'avatar': avatar})

def cursos(request):
    return render(request, "cursos.html")

def profesores(request):
    return render(request, "profesores.html")

def estudiantes(request):
    if request.method == "POST":
        estudiante = Estudiante(nombre = request.POST['nombre'], apellido = request.POST['apellido'], email = request.POST['email'])
        estudiante.save()
        avatar = Avatar.objects.filter(user = request.user.id)
        try:
            avatar = avatar[0].image.url
        except:
            avatar = None           
        return render(request, 'home.html', {'avatar': avatar})
    return render(request, "estudiantes.html")

def entregables(request):
    return render(request, "entregables.html")

def api_estudiantes(request):
    if request.method == "POST":
        formulario = form_estudiantes(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            estudiante = Estudiante( nombre = informacion['nombre'],apellido = informacion['apellido'], email = informacion['email'])
            estudiante.save()
            return render(request, "api_estudiantes.html")
    else:
        formulario = form_estudiantes()
    return render(request, "api_estudiantes.html", {"formulario": formulario})

def buscar_estudiantes(request):
    if request.GET["email"]: 
        email = request.GET["email"]
        estudiantes = Estudiante.objects.filter(email__icontains = email)           #filtro por emails en BD
        return render(request, "estudiantes.html", {"estudiantes": estudiantes})
    else:
        respuesta = "No se enviaron datos"
    return HttpResponse(respuesta)

def create_estudiantes(request):
    if request.method == "POST":
        estudiante = Estudiante(nombre = request.POST['nombre'], apellido = request.POST['apellido'], email = request.POST['email'])
        estudiante.save()     
        estudiantes = Estudiante.objects.all() #Trae todo
        return render(request, "estudiantesCRUD/read_estudiantes.html", {"estudiantes": estudiantes})
    return render(request, "estudiantesCRUD/create_estudiantes.html")

def read_estudiantes(request=None):
    estudiantes = Estudiante.objects.all() #Trae todo
    return render(request, "estudiantesCRUD/read_estudiantes.html", {"estudiantes": estudiantes})

def update_estudiantes(request, estudiante_id):
    estudiante = Estudiante.objects.get(id = estudiante_id)

    if request.method == 'POST':
        formulario = form_estudiantes(request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            estudiante.nombre = informacion['nombre']
            estudiante.apellido = informacion['apellido']
            estudiante.email = informacion['email']
            estudiante.save()
            estudiantes = Estudiante.objects.all() #Trae todo
            return render(request, "estudiantesCRUD/read_estudiantes.html", {"estudiantes": estudiantes})
    else:
        formulario = form_estudiantes(initial={'nombre': estudiante.nombre, 'apellido': estudiante.apellido, 'email': estudiante.email})
    return render(request,"estudiantesCRUD/update_estudiantes.html", {"formulario": formulario})
     

def delete_estudiantes(request, estudiante_id):
    estudiante = Estudiante.objects.get(id = estudiante_id)
    estudiante.delete()

    estudiantes = Estudiante.objects.all() #Trae todo
    return render(request, "estudiantesCRUD/read_estudiantes.html", {"estudiantes": estudiantes})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')

            user = authenticate(username = user, password = pwd)

            if user is not None:
                login(request, user)
                avatar = Avatar.objects.filter(user = request.user.id)
                try:
                    avatar = avatar[0].image.url
                except:
                    avatar = None           
                return render(request, 'home.html', {'avatar': avatar})
            else: 
                return render(request, "login.html", {'form':form})
        else:
             return render(request, "login.html", {'form':form}) 
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def registro(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            #username = form.cleaned_data["username"]
            form.save()
            return redirect("/Appcoder/login/")
        else: #decido regresar el formulario con error
            return render(request, "registro.html", {'form': form})

    #form = UserCreationForm()
    #else:
    form = UserRegisterForm()
    return render(request, "registro.html", {'form': form})

@login_required
def editarPerfil(request):
    usuario = request.user
    user_basic_info = User.objects.get(id = usuario.id)
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance = usuario)
        if form.is_valid():
            #Datos que se van a actualizar
            user_basic_info.username = form.cleaned_data.get('username')
            user_basic_info.email = form.cleaned_data.get('email')
            user_basic_info.first_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')
            user_basic_info.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None           
            return render(request, 'home.html', {'avatar': avatar})
        else:
            avatar = Avatar.objects.filter(user = request.user.id)
        try:
            avatar = avatar[0].image.url
        except:
            avatar = None           
        return render(request, 'home.html', {'avatar': avatar})
    else:
        form = UserEditForm(initial={'email': usuario.email, 'username': usuario.username, 'first_name': usuario.first_name, 'last_name': usuario.last_name })
    return render(request, 'editarPerfil.html', {'form': form, 'usuario': usuario})


@login_required
def changepass(request):
    usuario = request.user
    if request.method == 'POST':
        #form = PasswordChangeForm(data = request.POST, user = usuario)
        form = ChangePasswordForm(data = request.POST, user = request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None           
            return render(request, 'home.html', {'avatar': avatar})
    else:
        #form = PasswordChangeForm(request.user)
        form = ChangePasswordForm(user = request.user)
    return render(request, 'changepass.html', {'form': form, 'usuario': usuario})


@login_required
def perfilView(request):
    usuario = request.user
    user_basic_info = User.objects.get(id = usuario.id)
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None           
    print(usuario)
    return render(request, 'perfil.html',  {'avatar': avatar} )

'''{'form':user_basic_info},'''

def AgregarAvatar(request):
    if request.method == 'POST':
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.get(username = request.user)
            avatar = Avatar(user = user, image = form.cleaned_data['avatar'], id = request.user.id)
            avatar.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None           
            return render(request, 'home.html', {'avatar': avatar})
    else:
        try:
            avatar = Avatar.objects.filter(user = request.user.id)
            form = AvatarFormulario()
        except:
            form = AvatarFormulario()
    return render(request, 'AgregarAvatar.html', {'form': form})
