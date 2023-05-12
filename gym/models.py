from django.db import models

# Create your models here.

class TipoUsuario(models.Model):
    idTipo = models.AutoField(primary_key=True, verbose_name="ID del Tipo de Usuario")
    nombreTipo = models.CharField(max_length=30, verbose_name="Nombre Tipo de Usuario")

class Usuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=12, verbose_name="Rut del Usuario")
    nombre = models.CharField(max_length=35, verbose_name="Nombre del Usuario")
    apellido1 = models.CharField(max_length=30, verbose_name="Primer apellido del Usuario")
    apellido2 = models.CharField(max_length=30, verbose_name="Segundo apellido del Usuario")
    correo = models.EmailField(verbose_name="Correo del Usuario")
    contrasenia = models.CharField(null=True, max_length=30, verbose_name="Contraseña")
    tipoUsuario = models.ForeignKey(TipoUsuario, on_delete=models.SET_DEFAULT, default=0)
    fechaNacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    foto = models.ImageField(null=True, upload_to="\img", default="\img\avatar-redondo.png", verbose_name="Foto del Usuario")

class TipoFuncionario(models.Model):
    idTipoFuncionario = models.IntegerField(primary_key=True, verbose_name="ID del Tipo Funcionario")

class Funcionario(models.Model):
    idFuncionario = models.AutoField(primary_key=True, verbose_name="ID del Funcionario")
    cargo = models.CharField(max_length=20, verbose_name="Cargo del Funcionario")
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_DEFAULT, default=0)
    tipo = models.ForeignKey(TipoFuncionario, on_delete=models.SET_DEFAULT, default=0)

class Sucursal(models.Model):
    idSucursal = models.AutoField(primary_key=True, verbose_name="ID de la Sucursal")
    nombreSucursal = models.CharField(max_length=30, verbose_name="Nombre del Sucursal")
    direccionSucursal = models.CharField(max_length=50, verbose_name="Dirección de la Sucursal")

class Plan(models.Model):
    idPlan = models.AutoField(primary_key=True, verbose_name="ID del Plan")
    nombrePlan = models.CharField(max_length=30, verbose_name="Nombre del Plan")
    estadoPlan = models.BooleanField(verbose_name="Estado del Plan")
    sucursalLibre = models.BooleanField(verbose_name="Sucursal Libre")
    sucursal = models.ForeignKey(Sucursal, on_delete=models.SET_DEFAULT, default=0)

class Socio(models.Model):
    idSocio = models.AutoField(primary_key=True, verbose_name="ID del Socio")
    altura = models.IntegerField(verbose_name="Altura del Socio")
    peso = models.FloatField(verbose_name="Peso del Socio")
    observaciones = models.CharField(max_length=100, verbose_name="Observaciones")
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_DEFAULT, default=0)
    plan = models.ForeignKey(Plan, on_delete=models.SET_DEFAULT, default=0)
    titularPlan = models.CharField(max_length=30, verbose_name="Titular del Plan")

class Equipamiento(models.Model):
    idEquipamiento = models.AutoField(primary_key=True, verbose_name="ID del Equipamiento")
    sucursal = models.ForeignKey(Sucursal, on_delete=models.SET_DEFAULT, default=0)

class Reserva(models.Model):
    idReserva = models.AutoField(primary_key=True, verbose_name="ID de Reserva")
    fechaReserva = models.DateField(verbose_name="Fecha de la Reserva")
    horaReserva = models.TimeField(verbose_name="Hora de la Reserva")
    socio = models.ForeignKey(Socio, on_delete=models.SET_DEFAULT, default=0)
    equipamiento = models.ForeignKey(Equipamiento, on_delete=models.SET_DEFAULT, default=0)

class TipoProfesor(models.Model):
    idTipoProfesor = models.AutoField(primary_key=True, verbose_name="ID del Tipo de Profesor")
    nombreTipoProfesor = models.CharField(max_length=30, verbose_name="Nombre del Tipo de Profesor")

class Profesor(models.Model):
    idProfesor = models.AutoField(primary_key=True, verbose_name="ID del Profesor")
    fechaIngreso = models.DateField(verbose_name="Fecha de Ingreso")
    fechaContrato = models.DateField(verbose_name="Fecha de Contrato")
    tipo = models.ForeignKey(TipoProfesor, on_delete=models.SET_DEFAULT, default=0)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.SET_DEFAULT, default=0)

class Deporte(models.Model):
    idDeporte = models.AutoField(primary_key=True, verbose_name="ID del Deporte")
    nombreDeporte = models.CharField(max_length=30, verbose_name="Nombre del Deporte")

class DeporteProfesor(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_DEFAULT, default=0)
    deporte = models.ForeignKey(Deporte, on_delete=models.SET_DEFAULT, default=0)