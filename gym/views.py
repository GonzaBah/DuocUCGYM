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
    if(request.POST):
        ficha_form = FormFichaUsuario(request.POST or None)
        if ficha_form.is_valid():
            rut = ficha_form.cleaned_data.get('rut')
            user = get_user_model().objects.get(rut=rut)

            if not user and not user.is_sub:
                return redirect('ficha_socio')
            socio = Socio.objects.get(usuario = user)

            socio.altura = ficha_form.cleaned_data.get('estatura')
            socio.edad = ficha_form.cleaned_data.get('edad')
            socio.peso = ficha_form.cleaned_data.get('peso')
            socio.sucursal = Sucursal.objects.get(idSucursal = ficha_form.cleaned_data.get('sucursal'))
            socio.titularPlan = ficha_form.cleaned_data.get('titularPlan')
            socio.direccion = ficha_form.cleaned_data.get('direccion')
            socio.comuna = ficha_form.cleaned_data.get('comuna')
            socio.ciudad = ficha_form.cleaned_data.get('ciudad')
            socio.gSanguineo = ficha_form.cleaned_data.get('gSanguineo')
            socio.emergenciacontacto = ficha_form.cleaned_data.get('emergenciacontacto')
            socio.emergenciacontactoTel = ficha_form.cleaned_data.get('emergenciacontactoNumero')
            socio.pLesion =  ficha_form.cleaned_data.get('pLesion')
            socio.dLesion = ficha_form.cleaned_data.get('dLesion')
            socio.pEnfer =  ficha_form.cleaned_data.get('pEnfermedad')
            socio.dEnfer =  ficha_form.cleaned_data.get('dEnfermedad')
            socio.pDArtic =  ficha_form.cleaned_data.get('pArt')
            socio.dDArtic =  ficha_form.cleaned_data.get('dArt')
            socio.pDeporte =  ficha_form.cleaned_data.get('pDep')
            socio.dDeporte =  ficha_form.cleaned_data.get('dDep')
            socio.nDeporte =  ficha_form.cleaned_data.get('fDeportes')
            socio.diabetico =  ficha_form.cleaned_data.get('diabetico')
            socio.asmatico =  ficha_form.cleaned_data.get('asmatico')
            socio.epileptico =  ficha_form.cleaned_data.get('epileptico')
            socio.fumador =  ficha_form.cleaned_data.get('fumador')

            socio.save()

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
def list_plan(request):
    user = get_user_model().objects.get(correo = request.user)
    socio = Socio.objects.get(usuario=user)
    contexto = {
        "miPlan": Plan.objects.get(idPlan=socio.plan.idPlan)
    }
    return render(request, 'duoc_gym/planesMiPlan.html', contexto)

def borrar_plan(request, id):
    plan = Plan.objects.get(idPlan=id)
    plan.delete()

    return redirect('mtn_planes')

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

            messages.success(request, 'Plan registrado con éxito!!')
        return redirect('mtn_planes')
    except:
        messages.error(request, 'Hubo un error al registrar el Plan')
        return redirect('mtn_planes')

def prepa_alumno(request):
    return render(request, 'duoc_gym/preparacionAlumno.html')

def agregar_socio(request):
    return render(request, 'duoc_gym/agregarSocio.html')

@login_required(login_url='login')
def suscribir_plan(request, plan):
    plan = Plan.objects.get(idPlan = plan)
    user = get_user_model().objects.get(correo = request.user)
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
def mod_alumno(request, id):
    contexto = {
        "socioInfo": Socio.objects.get(idSocio = id)
    }
    return render(request, 'duoc_gym/frmModificarAlumnos.html', contexto)

@login_required(login_url='login')
def mod_perfil(request):
    user = get_user_model().objects.get(correo=request.user)
    tipo = TipoUsuario.objects.all()
    contexto = {
        "userInfo": user,
        "tipos": tipo
    }
    return render(request, 'duoc_gym/frmModificarUsuarios.html', contexto)


@login_required(login_url='login')
def mod_perfil_auth(request):
    try:
        user = get_user_model().objects.get(correo=request.user)
        if request.method == 'POST':
            rut = request.POST.get('rut')
            email = request.POST.get('correo')
            name = request.POST.get('nombre')
            lastname1 = request.POST.get('apellido1')
            lastname2 = request.POST.get('apellido2')
            fecha = request.POST.get('fechaNac')
            
            user.rut = rut
            user.correo=email
            user.nombre=name
            user.apellido1=lastname1
            user.apellido2=lastname2
            user.fechaNacimiento=fecha
            user.save()

            messages.success(request, 'Guardado con éxito!!')
    except:
        messages.error(request, 'Hubo un error al intentar Editar')
    return redirect('mi_perfil')

@login_required(login_url='login')
def mod_perfil_auth_admin(request):
    if request.method == 'POST':
        rut = request.POST.get('rut')
        email = request.POST.get('correo')
        name = request.POST.get('nombre')
        lastname1 = request.POST.get('apellido1')
        lastname2 = request.POST.get('apellido2')

        user = get_user_model().objects.get(rut=rut)
        
        user.rut = rut
        user.correo=email
        user.nombre=name
        user.apellido1=lastname1
        user.apellido2=lastname2
        user.save()

        messages.success(request, 'Guardado con éxito!!')
    return redirect('mtn_alumnos')

@login_required(login_url='login')
def mod_plan_auth(request, id):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        desc = request.POST.get('desc')
        sucursalLibre = request.POST.get('sucursalLibre')
        if sucursalLibre == 'on':
            sucursalLibre = True
        else:
            sucursalLibre = False
        precio = request.POST.get('precio')

        plan = Plan.objects.get(idPlan = id)
        plan.nombrePlan = nombre
        plan.descripcionPlan = desc
        plan.sucursalLibre = sucursalLibre
        plan.precio = precio

        plan.save()
    return redirect('mtn_planes')

@login_required(login_url='login')
def mod_curso_auth(request, id):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        sucursal = request.POST.get('sucursal')
        profesor = request.POST.get('profesor')
        deporte = request.POST.get('deporte')
        # if sucursalLibre == 'on':
        #     sucursalLibre = True
        # else:
        #     sucursalLibre = False
        # precio = request.POST.get('precio')

        curso = Curso.objects.get(idCurso = id)
        curso.nombreCurso = nombre
        curso.sucursal.nombreSucursal = sucursal
        curso.profesor.usuario.nombre = profesor
        curso.deporte.nombreDeporte = deporte

        curso.save()
        
    return redirect('mtn_cursos')

# @login_required(login_url="login")
# def mod_inventario_auth(request):
  
#     rut = request.POST.get('rut')
#     email = request.POST.get('correo')
#     name = request.POST.get('nombre')
#     lastname1 = request.POST.get('apellido1')
#     lastname2 = request.POST.get('apellido2')
    
    
#     user.rut = rut
#     user.correo=email
#     user.nombre=name
#     user.apellido1=lastname1
#     user.apellido2=lastname2
#     user.save()
#     return redirect('miPerfil')

@login_required(login_url='login')
def mtn_alumnos(request):
    profesor = Profesor.objects.get(usuario_id = request.user.rut)
    if profesor.usuario.tipoUsuario.nombreTipo == 'Coordinador de sucursal':
        socios = Socio.objects.filter(sucursal = profesor.sucursal)
    else:
        socios = Socio.objects.all()
    contexto = {
        "socios": socios
    }
    return render(request, 'duoc_gym/frmMantenedorAlumnos.html', contexto)

@login_required(login_url='login')
def mtn_clases(request):
    clases = claseCurso.objects.all()
    contexto = {
        "clases": clases
    }
    return render(request, 'duoc_gym/frmMantenedorClases.html',contexto)

@login_required(login_url='login')
def mtn_cursos(request):
    cursos = Curso.objects.all()
    contexto = {
        "cursos": cursos
    }
    return render(request, 'duoc_gym/frmMantenedorCursos.html',contexto)

@login_required(login_url='login')
def mtn_inventario(request):
    contexto = {
        "listaMaquinas": Equipamiento.objects.all()
    }
    return render(request,'duoc_gym/frmMantenedorInventario.html', contexto)

@login_required(login_url='login')
def mtn_planes(request):
    contexto = {
        "listaPlanes": Plan.objects.all()
    }
    return render(request, 'duoc_gym/frmMantenedorPlanes.html', contexto )

@login_required(login_url='login')
def mtn_usuarios(request):
    usuarios = Usuario.objects.all()
    contexto = {
        "usuarios": usuarios
    }
    return render(request, 'duoc_gym/frmMantenedorUsuarios.html', contexto)

@login_required(login_url='login')
def mtn_profesores(request):
    profesores = Profesor.objects.all()
    contexto = {
        "profesores": profesores
    }
    return render(request, 'duoc_gym/frmMantenedorProfesores.html', contexto)

@login_required(login_url='login')
def mod_alumno(request, rut):
    contexto = {
        "userInfo": get_user_model().objects.get(rut=rut)
    }
    return render(request, 'duoc_gym/frmModificarAlumnos.html', contexto)

@login_required(login_url='login')
def mod_clases(request, id):
    clase = claseCurso.objects.get(idClase = id)
    contexto = {
        "claseInfo": clase
    }
    return render(request, 'duoc_gym/frmModificarClases.html', contexto)

@login_required(login_url='login')
def mod_cursos(request, id):
    curso = Curso.objects.get(idCurso = id)
    contexto = {
        "cursoInfo": curso
    }
    return render(request, 'duoc_gym/frmModificarCursos.html', contexto)

def mod_usuarios(request,id):
    usuario = Usuario.objects.get( rut = id)
    contexto = {
        "usuarioInfo": usuario
    }
    return render(request, 'duoc_gym/frmModificarUsuarios.html',contexto)

def mod_profesores(request, id): 
    profesor = Profesor.objects.get( idProfesor = id)
    contexto = {
        "usuarioInfo": profesor
    }

    return render(request, 'duoc_gym/frmModificarProfesores.html',contexto)

def mod_planes(request, id):
    plan = Plan.objects.get(idPlan = id)
    contexto = {
        "planInfo": plan
    }
    return render(request, 'duoc_gym/frmModificarPlanes.html', contexto)

def mtn_fichas(request):
    contexto = {
        "fichas": Socio.objects.all()
    }
    return render(request, 'duoc_gym/frmMantenedorFichas.html',contexto)

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
def reporteProfesorTalleres(request):
    user = get_user_model().objects.get(correo = request.user)
    profesor = Profesor.objects.filter(usuario = user)
    month = datetime.datetime.now().month
    try:
        clases = claseCurso.objects.all()
        clasesHoy = list(filter(lambda x: x.mes() == month, clases))
        clasesProfe = list(filter(lambda x: x.curso.profesor == profesor, clases))

        print(clasesHoy)
        contexto = {
            "cursos": Curso.objects.get(profesor = profesor)
        }
        return render(request, "duoc_gym/profesorTalleres.html", contexto)
    except:
        return render(request, "duoc_gym/profesorTalleres.html")
    

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

def agregar_reserva_cancha(request):
    contexto = {
        "canchas": Cancha.objects.all()
    }
    return render(request, 'duoc_gym/agregarReservaCancha.html', contexto)

def reserva_view(request):
    if request.method == 'POST':
        user = get_user_model().objects.get(correo = request.user)
        socio = Socio.objects.get(usuario=user)
        clase = claseCurso.objects.get(idClase = request.POST.get("claseSelect"))
        
        if clase.is_available() == True and CursoReserva.objects.filter(socio=socio, clase=clase).count() == 0:
            cursoReserva = CursoReserva.objects.create(socio=socio, clase=clase)
            cursoReserva.save()
            messages.success(request, "Reserva creada exitosamente!!")
        else:
            messages.error(request, "Curso no tiene cupos o ya lo tomaste")
    return redirect('m_reservas')

def reserva_cancha_view(request, id):
    user = get_user_model().objects.get(correo = request.user)
    socio = Socio.objects.get(usuario=user)
    cancha = Cancha.objects.get(idCancha = id)

    if cancha.is_available() == True and CanchasReserva.objects.filter(socio=socio, cancha=cancha).count() == 0:
        canchaReserva = CanchasReserva.objects.create(socio=socio, cancha=cancha)
        canchaReserva.save()

        messages.success(request, "Reserva creada exitosamente!!")
    else:
        messages.error(request, "Cancha no tiene cupos o ya lo tomaste")
    return redirect('m_reservas_canchas')
def borrar_reserva(request, id):
    CursoReserva.objects.get(idCursoReserva = id).delete()

    return redirect('m_reservas')

def borrar_reserva_cancha(request, id):
    CanchasReserva.objects.get(idCanchareserva = id).delete()

    return redirect('m_reservas')

@login_required(login_url='login')
def reservas_canchas(request):
    socio = Socio.objects.get(usuario_id = request.user.rut)
    reservas = CanchasReserva.objects.filter(socio = socio)
    contexto = {
        "reservas": reservas
    }
    return render(request, 'duoc_gym/misReservasCanchas.html', contexto)