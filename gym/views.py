from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from .models import *
from .forms import *
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import redirect, render
import os
from django.contrib import messages
import datetime


# Create your views here.

def login_view(request):
    login_form = FormLoginUsuario(request.POST or None)
    if login_form.is_valid():
        email = login_form.cleaned_data.get('correo')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, correo=email, password=password)
        if user is not None:
            login(request, user)
            if(user.tipoUsuario == 1 or user.tipoUsuario == 2):
                return redirect('docente')
            else:
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
        
        user = get_user_model().objects.create(
            rut=rut,
            correo=email,
            nombre=name,
            apellido1=lastname1,
            password=make_password(password),
            apellido2=lastname2,
            tipoUsuario = TipoUsuario.objects.get(nombreTipo="Socio")
        )
        login(request, user)
        return redirect('index')

def logout_view(request):
    logout(request)
    return redirect('index')

def eliminar(request,id):
    messages.success(request, "desea eliminar nombreEntidad?")


def socio_view(request):
    try:
        ficha_form = FormFichaUsuario(request.POST or None)
        if ficha_form.is_valid():
            rut = ficha_form.cleaned_data.get('rut')
            if not get_user_model().objects.get(rut=rut) and not get_user_model().objects.get(rut=rut).is_sub:
                return redirect('ficha_socio')
            user = get_user_model().objects.get(rut=rut)
            socio = Socio.objects.get(usuario = user)
            altura = ficha_form.cleaned_data.get('altura')
            peso = ficha_form.cleaned_data.get('peso')
            fechaNac = ficha_form.cleaned_data.get('fechaNac')
            porcGrasa = ficha_form.cleaned_data.get('porcGrasa')
            observaciones = ficha_form.cleaned_data.get('observaciones')
            socio = Socio.objects.update(idSocio=socio.idSocio, usuario=user, altura=altura, peso=peso, porcGrasaCorporal=porcGrasa, observaciones=observaciones)
            socio.save()
            user.fechaNacimiento = fechaNac
            user.save()
        return redirect('lista')
    except:
        return redirect('lista')

def borrar_socio(request, id):
    socio = Socio.objects.get(idSocio=id)
    socio.delete()

    return redirect('lista')

def index(request):
    return render(request, 'duoc_gym/index.html')

def login_usuario(request):
    return render(request, 'duoc_gym/login.html')

@login_required(login_url='login')
def index_docente(request):
    return render(request, 'duoc_gym/indexDocente.html')



def socio_reg(request):
    return render(request, 'duoc_gym/sociosRegistrarse.html')

def fic_socio(request):
    sucursales = Sucursal.objects.all()
    contexto = {
        "sucursales": sucursales
    }
    return render(request, 'duoc_gym/fichaSocio.html', contexto)

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



def borrar_plan(request, id):
    plan = Plan.objects.get(idPlan=id)
    plan.delete()

    return redirect('m_planes')

def agregar_plan(request):
    return render(request, 'duoc_gym/agregarPlan.html')

def plan_view(request):
    try:
        plan_form = FormRegisPlan(request.POST or None)
        if plan_form.is_valid():
            nombre = plan_form.cleaned_data.get('nombre')
            descripcion = plan_form.cleaned_data.get('descripcion')
            sucursalLibre = plan_form.cleaned_data.get('sucursalLibre')
            precio = plan_form.cleaned_data.get('precio')
            
            plan = Plan.objects.create(nombrePlan=nombre, estadoPlan=True, descripcionPlan=descripcion, sucursalLibre=sucursalLibre, precio=precio)
            plan.save()
        return redirect('m_planes')
    except:
        return redirect('agregar_p')

def prepa_alumno(request):
    return render(request, 'duoc_gym/preparacionAlumno.html')

def agregar_socio(request):
    return render(request, 'duoc_gym/agregarSocio.html')



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


@login_required(login_url='login')
def mi_perfil(request):
    usuario = Usuario.objects.get(correo=request.user)
    try:
        contexto = {
            "socioInfo": Socio.objects.get(usuario=usuario)
        }
        return render(request,'duoc_gym/miPerfil.html', contexto)
    except:
        return render(request, 'duoc_gym/miPerfil.html')


@login_required(login_url='login')
def reportes(request):
        return render(request, 'duoc_gym/reportes.html')



@login_required(login_url='login')
def mod_alumno(request):
    contexto = {
        "userInfo": Usuario.objects.get(correo=request.user)
    }
    return render(request, 'duoc_gym/frmAlumnosModificar.html', contexto)

@login_required(login_url='login')
def mod_perfil_auth(request):
    user = get_user_model().objects.get(rut=request.user.rut)

    rut = request.POST.get('rut')
    email = request.POST.get('correo')
    name = request.POST.get('nombre')
    lastname1 = request.POST.get('apellido1')
    lastname2 = request.POST.get('apellido2')
    
    user.rut = rut
    user.correo=email
    user.nombre=name
    user.apellido1=lastname1
    user.apellido2=lastname2
    user.save()
    return redirect('mi_perfil')

def mod_plan_auth(request):
    rut = request.POST.get('rut')
    email = request.POST.get('correo')
    name = request.POST.get('nombre')
    lastname1 = request.POST.get('apellido1')
    lastname2 = request.POST.get('apellido2')
    
    user = get_user_model().objects.update_or_create(
        rut=rut,
        correo=email,
        nombre=name,
        apellido1=lastname1,
        apellido2=lastname2
    )
    user.save()
    return redirect('mi_perfil')

@login_required(login_url="login")
def mod_inventario_auth(request):
  
    rut = request.POST.get('rut')
    email = request.POST.get('correo')
    name = request.POST.get('nombre')
    lastname1 = request.POST.get('apellido1')
    lastname2 = request.POST.get('apellido2')
    
    user = get_user_model().objects.get(rut=request.user.rut)
    user.rut = rut
    user.correo=email
    user.nombre=name
    user.apellido1=lastname1
    user.apellido2=lastname2
    user.save()
    return redirect('miPerfil')

def mtn_alumnos(request):
    socios = Socio.objects.all()
    contexto = {
        "socios": socios
    }
    return render(request, 'duoc_gym/frmMantenedorAlumnos.html', contexto)

def mtn_clases(request):
    clases = claseCurso.objects.all()
    contexto = {
        "clases": clases
    }
    return render(request, 'duoc_gym/frmMantenedorClases.html',contexto)

def mtn_cursos(request):
    cursos = Curso.objects.all()
    contexto = {
        "cursos": cursos
    }
    return render(request, 'duoc_gym/frmMantenedorCursos.html',contexto)

def mtn_inventario(request):
    contexto = {
        "listaMaquinas": Equipamiento.objects.all()
    }
    return render(request,'duoc_gym/frmMantenedorInventario.html', contexto)

def mtn_planes(request):
    contexto = {
        "listaPlanes": Plan.objects.all()
    }
    return render(request, 'duoc_gym/frmMantenedorPlanes.html', contexto )

def mtn_usuarios(request):
    usuarios = Usuario.objects.all()
    contexto = {
        "usuarios": usuarios
    }
    return render(request, 'duoc_gym/frmMantenedorUsuarios.html', contexto)

def mtn_profesores(request):
    profesores = Profesor.objects.all()
    contexto = {
        "profesores": profesores
    }
    return render(request, 'duoc_gym/frmMantenedorProfesores.html', contexto)

@login_required(login_url='login')
def mod_alumno(request):
    contexto = {
        "userInfo": Usuario.objects.get(correo=request.user)
    }
    return render(request, 'duoc_gym/frmModificarAlumnos.html', contexto)

def mod_clases(request):
    # if(request.POST):
    #     user = get_user_model().objects.get(correo = request.user)

    #     clase = claseCurso.objects.get(idClase = user)

    #     if clase.is_available:
    #         claseCurso.objects.create(clase=clase)
    #         claseCurso.save()
        
    #     else:
    #         pass

    # return redirect('mtn_clases')
    return render(request, 'duoc_gym/frmModificarClases.html')

def mod_cursos(request):
    return render(request, 'duoc_gym/frmModificarCursos.html')

def mod_usuarios(request):
    return render(request, 'duoc_gym/frmModificarUsuarios.html')

def mod_profesores(request): 
    return render(request, 'duoc_gym/frmModificarProfesores.html')

def rpt_planes(request):
    contexto = {
        "listaPlanes": Plan.objects.all()
    }
    return render(request, 'duoc_gym/reportePlanes.html',contexto)

@login_required(login_url="login")
def reservas(request):
    user = get_user_model().objects.get(correo = request.user)
    try:
        socio = Socio.objects.get(usuario=user)
        contexto = {
            "reservas": CursoReserva.objects.filter(socio=socio)
        }
        return render(request, "duoc_gym/misReservas.html", contexto)
    except:
        return render(request, "duoc_gym/misReservas.html")

@login_required(login_url="login")
def reporteProfesor(request):
    month = datetime.datetime.now().month
    try:
        clases = claseCurso.objects.all()
        clasesHoy = list(filter(lambda x: x.mes() == month, clases))
        print(clasesHoy)
        contexto = {
            
            "cursos": Curso.objects.all() 
        }
        return render(request, "duoc_gym/reporteProfesor.html", contexto)
    except:
        return render(request, "duoc_gym/reporteProfesor.html")
@login_required(login_url="login")
def reporteSocioMes(request):
    try:
        socio = Socio.objects.all()
        for i in socio:
            print(i.count_socioMes)
            print(i.usuario.nombre)
        contexto = {
            "socios": socio
        }
        return render(request, "duoc_gym/reporteSocioMes.html", contexto)
    except:
        return render(request, "duoc_gym/reporteSocioMes.html")

def reporteReservasMes(request):
    try:

        cursos = Curso.objects.all()
        contexto = {
            "cursos": cursos
        }
        return render(request, "duoc_gym/reporteReservasMes.html", contexto)
    except:
        return render(request, "duoc_gym/reporteReservasMes.html")


def agregar_reserva(request):
    try:
        contexto = {
            "cursos": Curso.objects.all(),
            "clases": claseCurso.objects.all()
        }
    except:
        contexto = {
            "cursos": Curso.objects.all()
        }
    return render(request, 'duoc_gym/agregarReserva.html', contexto)
    
def reserva_view(request):
    if(request.POST):
        user = get_user_model().objects.get(correo = request.user)
        socio = Socio.objects.get(usuario=user)
        clase = claseCurso.objects.get(idClase = request.POST.get("claseSelect"))
        
        if clase.is_available() == True and CursoReserva.objects.filter(socio=socio, clase=clase).count() == 0:
            cursoReserva = CursoReserva.objects.create(socio=socio, clase=clase)
            cursoReserva.save()
            messages.success(request, "Reserva creada exitosamente")
        else:
            messages.error(request, "Curso no tiene cupos o ya lo tomaste")
    return redirect('m_reservas')

def borrar_reserva(request, id):
    CursoReserva.objects.get(idCursoReserva = id).delete()

    return redirect('m_reservas')
