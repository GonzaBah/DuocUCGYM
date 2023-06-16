from django.conf import settings
from django.db import models
from django.utils.text import slugify
import random
import string
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
import datetime
# Create your models here.

def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

class CustomAccountManager(BaseUserManager):
    def create_user(self, correo, nombre, apellido1, rut, password, **other_fields):
        if not correo:
            raise ValueError(('Error: Falta un correo'))
        correo = self.normalize_email(correo)
        user = self.model(correo=correo, nombre=nombre, apellido1=apellido1, rut=rut, **other_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, correo, nombre, apellido1, rut, password, **other_fields):
        rol_admin = TipoUsuario.objects.get(nombreTipo="Administrador del sistema")
        other_fields.setdefault('tipoUsuario', rol_admin)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser debe ser True')
        if other_fields.get('tipoUsuario') is not rol_admin:
            raise ValueError(
                'Superuser debe ser tipo Funcionario')
        return self.create_user(correo, nombre, apellido1, rut, password, **other_fields)

class TipoUsuario(models.Model):
    idTipo = models.AutoField(primary_key=True, verbose_name="ID del Tipo de Usuario")
    nombreTipo = models.CharField(max_length=30, verbose_name="Nombre Tipo de Usuario")

class Usuario(AbstractBaseUser, PermissionsMixin):
    rut = models.CharField(primary_key=True, max_length=12, verbose_name="Rut del Usuario")
    nombre = models.CharField(max_length=35, verbose_name="Nombre del Usuario")
    apellido1 = models.CharField(max_length=30, verbose_name="Primer apellido del Usuario")
    apellido2 = models.CharField(max_length=30, verbose_name="Segundo apellido del Usuario", null=True )
    correo = models.EmailField(verbose_name="Correo del Usuario", unique=True)
    tipoUsuario = models.ForeignKey(TipoUsuario, on_delete=models.SET_DEFAULT, default=6)
    fechaNacimiento = models.DateField(verbose_name="Fecha de Nacimiento", null=True)

    is_sub = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    # slug = models.SlugField(max_length=255, default="", null=False, unique=True)
    
    foto = models.ImageField(null=True, upload_to="\img", default="\img\avatar-redondo.png", verbose_name="Foto del Usuario")
    
    objects = CustomAccountManager()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['rut', 'nombre', 'apellido1']

    def __str__(self):
            return f'{self.correo}'
    def save(self, *args, **kwargs):
        """ if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.correo) """
        super(Usuario, self).save(*args, **kwargs)

class TipoFuncionario(models.Model):
    idTipoFuncionario = models.IntegerField(primary_key=True, verbose_name="ID del Tipo Funcionario")
class Funcionario(models.Model):
    idFuncionario = models.AutoField(primary_key=True, verbose_name="ID del Funcionario")
    cargo = models.CharField(max_length=20, verbose_name="Cargo del Funcionario")
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=1)
    tipo = models.ForeignKey(TipoFuncionario, on_delete=models.SET_DEFAULT, default=1)
class Sucursal(models.Model):
    idSucursal = models.AutoField(primary_key=True, verbose_name="ID de la Sucursal")
    nombreSucursal = models.CharField(max_length=30, verbose_name="Nombre del Sucursal")
    direccionSucursal = models.CharField(max_length=50, verbose_name="Dirección de la Sucursal")
class Plan(models.Model):
    idPlan = models.AutoField(primary_key=True, verbose_name="ID del Plan")
    nombrePlan = models.CharField(max_length=30, verbose_name="Nombre del Plan")
    estadoPlan = models.BooleanField(verbose_name="Estado del Plan")
    descripcionPlan = models.CharField(max_length=500, verbose_name="Descripcion del Plan", null=True)
    sucursalLibre = models.BooleanField(verbose_name="Sucursal Libre")
    precio = models.IntegerField(verbose_name="Precio del plan", default=1)
class Socio(models.Model):
    idSocio = models.AutoField(primary_key=True, verbose_name="ID del Socio")
    edad = models.IntegerField(verbose_name="edad del Socio", null=True)
    altura = models.IntegerField(verbose_name="altura del Socio", null=True)
    peso = models.IntegerField(verbose_name="peso del Socio", null=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=1)
    plan = models.ForeignKey(Plan, on_delete=models.SET_DEFAULT, default=1)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.SET_NULL, null=True)
    titularPlan = models.CharField(max_length=30, verbose_name="Titular del Plan", null=True)
    direccion = models.CharField(max_length=125, verbose_name="Direccion", null=True)
    comuna = models.CharField(max_length=35, verbose_name="comuna", null=True)
    ciudad = models.CharField(max_length=35, verbose_name="ciudad", null=True)
    gSanguineo = models.CharField(max_length=3, verbose_name="Grupo sanguineo", null=True)
    emergenciacontacto = models.CharField(max_length=35, verbose_name="Nombre de contacto a llamar en caso d emergencia", null=True)
    emergenciacontactoTel = models.CharField(max_length=10, verbose_name="Telefono de contacto a llamar en caso d emergencia", null=True)
    pLesion =  models.BooleanField(default=False, verbose_name="Posee lesiones?")
    dLesion = models.CharField(max_length=200, verbose_name="Descripcion lesiones", null=True)
    pEnfer =  models.BooleanField(default=False,verbose_name="Posee enfermedades prexistentes?")
    dEnfer =  models.CharField(max_length=200, verbose_name="Descripcion enfermedades prexistentes", null=True)
    pDArtic =  models.BooleanField(default=False,verbose_name="Posee dolores en las articulaciones?")
    dDArtic =  models.CharField(max_length=200, verbose_name="Descripcion dolores en las articulaciones?", null=True)
    pDeporte =  models.BooleanField(default=False,verbose_name="Practica algun deporte?")
    dDeporte =  models.CharField(max_length=200, verbose_name="Cuales?", null=True)
    nDeporte =  models.IntegerField(default=0, verbose_name="Veces a la semana que hace deportes", null=True)
    diabetico =  models.BooleanField(default=False,verbose_name="es usted diabetico?")
    asmatico =  models.BooleanField(default=False,verbose_name="es usted asmatico?")
    epileptico =  models.BooleanField(default=False,verbose_name="es usted epiliptico?")
    fumador =  models.BooleanField(default=False,verbose_name="fuma?")
    def count_socioMes(self):
        month = datetime.datetime.now().month
        clases = CursoReserva.objects.all()
        clasesMes = list(filter(lambda x: x.clase.mes() == month, clases))
        return len(list(filter(lambda x: x.socio == self, clasesMes)))
    
class Equipamiento(models.Model):
    idEquipamiento = models.AutoField(primary_key=True, verbose_name="ID del Equipamiento")
    nombreEquipamiento = models.CharField(max_length=30, verbose_name="Nombre del Equipamiento")
    sucursal = models.ForeignKey(Sucursal, on_delete=models.SET_DEFAULT, default=1)
class Reserva(models.Model):
    idReserva = models.AutoField(primary_key=True, verbose_name="ID de Reserva")
    socio = models.ForeignKey(Socio, on_delete=models.SET_DEFAULT, default=1)
class Profesor(models.Model):
    idProfesor = models.AutoField(primary_key=True, verbose_name="ID del Profesor")
    fechaIngreso = models.DateField(verbose_name="Fecha de Ingreso")
    fechaContrato = models.DateField(verbose_name="Fecha de Contrato")
    sucursal = models.ForeignKey(Sucursal, on_delete=models.SET_DEFAULT, default=1)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)


class Deporte(models.Model):
    idDeporte = models.AutoField(primary_key=True, verbose_name="ID del Deporte")
    nombreDeporte = models.CharField(max_length=30, verbose_name="Nombre del Deporte")
class DeporteProfesor(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_DEFAULT, default=1)
    deporte = models.ForeignKey(Deporte, on_delete=models.SET_DEFAULT, default=1)
class Curso(models.Model):
    idCurso = models.AutoField(primary_key=True, verbose_name="ID del curso")
    nombreCurso = models.CharField(max_length=30, verbose_name="Nombre del curso")
    sucursal = models.ForeignKey(Sucursal, on_delete=models.SET_DEFAULT, default=1)
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_DEFAULT, default=1)
    deporte = models.ForeignKey(Deporte, on_delete=models.SET_DEFAULT, default=1)
    def count_profeMes(self):
        month = datetime.datetime.now().month
        clases = claseCurso.objects.filter( curso = self)
        return len(list(filter(lambda x: x.mes() == month, clases)))


class Cancha(models.Model):
    idCancha = models.AutoField(primary_key=True, verbose_name="ID del cancha")
    deporte = models.ForeignKey(Deporte, on_delete=models.SET_DEFAULT, default=1)
    cupo = models.IntegerField(verbose_name="tope de alumnos en la cancha", default=30)    
    sucursal = models.ForeignKey(Sucursal, on_delete=models.SET_DEFAULT, default=1)

class CanchasReserva(models.Model):
    idCanchareserva = models.AutoField(primary_key=True, verbose_name="ID del cancha reserva")
    reserva = models.ForeignKey(Reserva, on_delete=models.SET_DEFAULT, default=1)
    cancha = models.ForeignKey(Cancha, on_delete=models.SET_DEFAULT, default=1)

class claseCurso(models.Model):
    idClase = models.AutoField(primary_key=True, verbose_name="ID del clase reserva")
    fechaClase= models.DateField(verbose_name="Fecha de la Reserva")
    horaClase = models.TimeField(verbose_name="Hora de la Reserva")
    curso = models.ForeignKey(Curso, on_delete=models.SET_DEFAULT, default=1)
    cupo = models.IntegerField(verbose_name="tope de alumnos en la clase", default=30)

    def cupos(self):
        return CursoReserva.objects.filter(clase_id = self.idClase).count()
    def is_available(self):
        return CursoReserva.objects.filter(clase_id = self.idClase).count() <= self.cupo
    def mes(self):
        return self.fechaClase.month
class CursoReserva(models.Model):
    idCursoReserva = models.AutoField(primary_key=True, verbose_name="ID del curso reserva")
    socio = models.ForeignKey(Socio, on_delete=models.SET_DEFAULT, default=1)
    clase = models.ForeignKey(claseCurso, on_delete=models.SET_DEFAULT, default=1)
