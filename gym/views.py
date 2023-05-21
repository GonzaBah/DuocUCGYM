from django.shortcuts import render
from .models import *

# Create your views here.

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