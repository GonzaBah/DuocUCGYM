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
    path('logIn', login_usuario, name='login'),
    path('login_auth', login_view, name='login_auth'),
    path('logout', logout_view, name='logout'),
    path('signup_auth', signup_view, name='signup_auth'),
    path('socios_reg', socio_reg, name='socios_registrarse'),
    path('suscribir_plan/<str:user>/<int:plan>', suscribir_plan, name='suscribir_plan'),
    path('mi_perfil',mi_perfil, name='mi_perfil'),

    path('docente', index_docente, name='docente'),
    path('lista_alumnos', lista_alumnos, name='lista'),
    
    path('mantener_planes', mantenedor_planes, name='m_planes'),
    path('agregar_plan', agregar_plan, name='agregar_p'),
    path('plan_auth', plan_view, name='plan_auth'),
    path('mantener_maquinas', mantenedor_maquinas, name='m_maquinas'),
    path('borrar_plan/<int:id>', borrar_plan, name='borrar_p'),
    path('planes_alumnos', planes_alumnos, name='plan'),
    path('borrar_socio/<int:id>', borrar_socio, name='borrar_socio'),

    path('ficha_socio', fic_socio, name='ficha_socio'),
    path('agr_socio', agregar_socio, name='a_socio'),
    path('socio_auth', socio_view, name='socio_auth'),

    path('prepa_alumno',prepa_alumno, name='p_alumno'),
    path('descripcion_plan', desc_plan, name='d_plan'),
    path('miplan/<str:user>', list_plan, name='l_plan'),

    path('m_alumno', mod_alumno, name='mAlumno'),
    path('m_perfil_auth', mod_perfil_auth, name='m_perfil_auth'),

    path('rpt_planes', rpt_planes, name =  'rpt_planes'),
    path('m_reservas', reservas, name='m_reservas'),
    path('agr_reserva', agregar_reserva, name='a_reserva'),
    path('reserva_auth', reserva_view, name='reserva_auth')
 ]