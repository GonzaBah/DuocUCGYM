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
            return redirect('login')

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

def fic_socio(request):
    return render(request, 'duoc_gym/fichaSocio.html')

def planes_alumnos(request):  
    contexto = {
        "listaPlanes": Plan.objects.all()
    }
    return render(request, 'duoc_gym/planesAlumnos.html', contexto)

def desc_plan(request):
    return render(request, 'duoc_gym/descripcionPlan.html')

@login_required(login_url='login')
def list_plan(request, user):
    user = get_user_model().objects.get(correo = user)
    socio = Socio.objects.get(usuario=user)
    contexto = {
        "miPlan": Plan.objects.get(idPlan=socio.plan.idPlan)
    }
    return render(request, 'duoc_gym/planesMiPlan.html', contexto)

def mantenedor_planes(request):
    return render(request, 'duoc_gym/mantenedorPlanes.html' )

def prepa_alumno(request):
    return render(request, 'duoc_gym/preparacionAlumno.html')

def agregar_socio(request):
    return render(request, 'duoc_gym/agregarSocio.html')

def mantenedor_maquinas(request):
    return render(request,'duoc_gym/inventarioMaquinas.html')

def suscribir_plan(request, user, plan):
    plan = Plan.objects.get(idPlan = plan)
    user = get_user_model().objects.get(correo = user)
    if (user.is_sub == False):
        user.is_sub = True
        socio = Socio.objects.create(plan=plan, usuario=user)
        socio.save()
        user.save()
        return redirect('index')
    else:
        return redirect('plan')
