from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import FormLoginUsuario
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import redirect, render

# Create your views here.

def login_view(request):
    login_form = FormLoginUsuario(request.POST or None)
    if login_form.is_valid():
        email = login_form.cleaned_data.get('correo')
        password = login_form.cleaned_data.get('contrasenia')
        user = authenticate(request, correo=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Has iniciado sesion correctamente')
            return redirect('index')
        else:
            messages.error(request, "Error: Usuario o contraseña inválidos (╬ Ò﹏Ó)!")
            return redirect('socios_registrarse')

    # messages.error(request, 'Formulario Invalido')
    return redirect('index')

def index(request):
    return render(request, 'duoc_gym/index.html')

def login(request):
    return render(request, 'duoc_gym/login.html')

def index_docente(request):
    return render(request, 'duoc_gym/indexDocente.html')

def lista_alumnos(request):
    return render(request, 'duoc_gym/listaAlumnos.html')

def socio_reg(request):
    return render(request, 'duoc_gym/sociosRegistrarse.html')

def planes_alumnos(request):
    return render(request, 'duoc_gym/planesAlumnos.html')

def desc_plan(request):
    return render(request, 'duoc_gym/descripcionPlan.html')

def list_plan(request):
    return render(request, 'duoc_gym/planesMiPlan.html')

def mantenedor_planes(request):
    return render(request, 'duoc_gym/mantenedoPlanes.html' )

def prepa_alumno(request):
    return render(request, 'duoc_gym/preparacionAlumno.html')
