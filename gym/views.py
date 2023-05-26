from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from .models import *
from .forms import *
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import redirect, render
import os

# Create your views here.

def login_view(request):
    login_form = FormLoginUsuario(request.POST or None)
    if login_form.is_valid():
        email = login_form.cleaned_data.get('correo')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, correo=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Error: Usuario o contraseña inválidos (╬ Ò﹏Ó)!")
            return redirect('socios_registrarse')

    # messages.error(request, 'Formulario Invalido')
    return redirect('index')

def signup_view(request):
    signup_form = FormRegisUsuario(request.POST or None)
    if signup_form.is_valid():
        rut = signup_form.cleaned_data.get('rut')
        email = signup_form.cleaned_data.get('correo')
        name = signup_form.cleaned_data.get('nombre')
        lastname1 = signup_form.cleaned_data.get('apellido1')
        lastname2 = signup_form.cleaned_data.get('apellido2')
        password = signup_form.cleaned_data.get('password')
        
        print(rut + email + name + lastname1 + lastname2)
        user = get_user_model().objects.create(
            rut=rut,
            correo=email,
            nombre=name,
            apellido1=lastname1,
            password=make_password(password),
            apellido2=lastname2,
            tipoUsuario = TipoUsuario.objects.get(idTipo = 3)
        )
        login(request, user)
        return redirect('index')

def logout_view(request):
    logout(request)
    return redirect('index')

def index(request):
    return render(request, 'duoc_gym/index.html')

def login_usuario(request):
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
    return render(request, 'duoc_gym/mantenedorPlanes.html' )

def prepa_alumno(request):
    return render(request, 'duoc_gym/preparacionAlumno.html')

def agregar_socio(request):
    return render(request, 'duoc_gym/agregarSocio.html')

def mantenedor_maquinas(request):
    return render(request,'duoc_gym/inventarioMaquinas.html')
