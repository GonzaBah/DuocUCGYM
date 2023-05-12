from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request, 'duoc_gym/index.html')

def index_docente(request):
    return render(request, 'duoc_gym/index_docente.html')

def lista_alumnos(request):
    return render(request, 'duoc_gym/lista_alumnos.html')

def socio_reg(request):
    return render(request, 'duoc_gym/socios_registrarse.html')

def planes_alumnos(request):
    listaPlanes = Plan.objects.all()
    contexto = {
        "listaPlanes": listaPlanes
    }
    return render(request, 'duoc_gym/planes_alumnos.html', contexto)

def desc_plan(request):
    return render(request, 'duoc_gym/descripcion_plan.html')

def list_plan(request):
    return render(request, 'duoc_gym/planes_miplan.html')