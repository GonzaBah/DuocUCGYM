from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'duoc_gym/index.html')

def index_docente(request):
    return render(request, 'duoc_gym/index_docente.html')

def lista_alumnos(request):
    return render(request, 'duoc_gym/lista_alumnos.html')

def socio_reg(request):
    return render(request, 'duoc_gym/socios_registrarse.html')