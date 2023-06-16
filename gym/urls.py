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
   
    path('agregar_plan', agregar_plan, name='agregar_p'),
    path('plan_auth', plan_view, name='plan_auth'),
  
    path('borrar_plan/<int:id>', borrar_plan, name='borrar_p'),
    path('planes_alumnos', planes_alumnos, name='plan'),
    path('borrar_socio/<int:id>', borrar_socio, name='borrar_socio'),

    path('ficha_socio', fic_socio, name='ficha_socio'),
    path('agr_socio', agregar_socio, name='a_socio'),
    path('socio_auth', socio_view, name='socio_auth'),

    path('prepa_alumno',prepa_alumno, name='p_alumno'),
    path('descripcion_plan', desc_plan, name='d_plan'),
    path('miplan/<str:user>', list_plan, name='l_plan'),

    path('mtn_inventario', mtn_inventario, name='mtn_inventario'),
    path('mtn_alumnos', mtn_alumnos, name='mtn_alumnos'),
    path('mtn_planes', mtn_planes, name='mtn_planes'),
    path('mtn_clases', mtn_clases, name='mtn_clases'),
    path('mtn_cursos', mtn_cursos, name='mtn_cursos'),
    path('mtn_usuarios', mtn_usuarios, name='mtn_usuarios'),
    path('mtn_profesores', mtn_profesores, name='mtn_profesores'),

    path('mod_clases', mod_clases, name='mod_clases'),
    path('mod_cursos', mod_cursos, name='mod_cursos'),
    path('mod_usuarios', mod_usuarios, name='mod_usuarios'),
    path('mod_profesores', mod_profesores, name='mod_profesores'),
    path('mod_alumno', mod_alumno, name='mod_alumnos'),
    path('mod_perfil_auth', mod_perfil_auth, name='mod_perfil_auth'),
    path('mod_perfil', mod_perfil,name = 'mod_perfil'),

    # path('mtn_fichas', mtn_fichas, name =  'mtn_fichas'),
    path('m_reservas', reservas, name='m_reservas'),
    path('agr_reserva', agregar_reserva, name='a_reserva'),
    path('reserva_auth', reserva_view, name='reserva_auth'),
    path('b_reserva/<int:id>', borrar_reserva, name='b_reserva'),
    path('reporte_profesor', reporteProfesor, name='reporte_profesor'),
    path('reporte_socio_mes', reporteSocioMes, name='reporte_socio_mes'),
    path('reporte_reservas_mes', reporteReservasMes, name='reporte_reservas_mes'),
        path('reportes', reportes, name='reportes')

 ]