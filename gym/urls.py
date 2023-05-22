"""bakaNeko_site URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('logIn', login, name='login'),
    path('docente', index_docente, name='docente'),
    path('lista_alumnos', lista_alumnos, name='lista'),
   
    path('planes_alumnos', planes_alumnos, name='plan'),
    path('socios_reg', socio_reg, name='socios_registrarse'),
    path('descripcion_plan', desc_plan, name='d_plan'),
    path('lista_miplan', list_plan, name='l_plan'),

    path('mantener_planes', mantenedor_planes, name='m_planes')


 ]