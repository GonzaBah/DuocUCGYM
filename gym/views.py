from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request, 'duoc_gym/index.html')

def login(request):
    return render(request, 'duoc_gym/login.html')

def index_docente(request):
    return render(request, 'duoc_gym/index_docente.html')

def lista_alumnos(request):
    return render(request, 'duoc_gym/lista_alumnos.html')

def socio_reg(request):
    return render(request, 'duoc_gym/socios_registrarse.html')

def planes_alumnos(request):  
    return render(request, 'duoc_gym/planes_alumnos.html')

def desc_plan(request):
    return render(request, 'duoc_gym/descripcion_plan.html')

def list_plan(request):
    return render(request, 'duoc_gym/planes_miplan.html')

def mantenedor_planes(request):
    return render(request, 'duoc_gym/mantenedor_planes.html' )

def prepa_alumno(request):
    return render(request, 'duoc_gym/preparacion_alumno.html')

def agregar_socio(request):
    return render(request, 'duoc_gym/agregar_socio.html')

def mantenedor_maquinas(request):
    return render(request,'duoc_gym/inventario_maquinas.html')