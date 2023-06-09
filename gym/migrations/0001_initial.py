# Generated by Django 4.2.2 on 2023-06-15 03:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('rut', models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='Rut del Usuario')),
                ('nombre', models.CharField(max_length=35, verbose_name='Nombre del Usuario')),
                ('apellido1', models.CharField(max_length=30, verbose_name='Primer apellido del Usuario')),
                ('apellido2', models.CharField(max_length=30, null=True, verbose_name='Segundo apellido del Usuario')),
                ('correo', models.EmailField(max_length=254, unique=True, verbose_name='Correo del Usuario')),
                ('fechaNacimiento', models.DateField(null=True, verbose_name='Fecha de Nacimiento')),
                ('is_sub', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('foto', models.ImageField(default='\\img\x07vatar-redondo.png', null=True, upload_to='\\img', verbose_name='Foto del Usuario')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cancha',
            fields=[
                ('idCancha', models.AutoField(primary_key=True, serialize=False, verbose_name='ID del cancha')),
                ('cupo', models.IntegerField(default=30, verbose_name='tope de alumnos en la cancha')),
            ],
        ),
        migrations.CreateModel(
            name='claseCurso',
            fields=[
                ('idClase', models.AutoField(primary_key=True, serialize=False, verbose_name='ID del clase reserva')),
                ('fechaClase', models.DateField(verbose_name='Fecha de la Reserva')),
                ('horaClase', models.TimeField(verbose_name='Hora de la Reserva')),
                ('cupo', models.IntegerField(default=30, verbose_name='tope de alumnos en la clase')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('idCurso', models.AutoField(primary_key=True, serialize=False, verbose_name='ID del curso')),
                ('nombreCurso', models.CharField(max_length=30, verbose_name='Nombre del curso')),
            ],
        ),
        migrations.CreateModel(
            name='Deporte',
            fields=[
                ('idDeporte', models.AutoField(primary_key=True, serialize=False, verbose_name='ID del Deporte')),
                ('nombreDeporte', models.CharField(max_length=30, verbose_name='Nombre del Deporte')),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('idPlan', models.AutoField(primary_key=True, serialize=False, verbose_name='ID del Plan')),
                ('nombrePlan', models.CharField(max_length=30, verbose_name='Nombre del Plan')),
                ('estadoPlan', models.BooleanField(verbose_name='Estado del Plan')),
                ('descripcionPlan', models.CharField(max_length=500, null=True, verbose_name='Descripcion del Plan')),
                ('sucursalLibre', models.BooleanField(verbose_name='Sucursal Libre')),
                ('precio', models.IntegerField(default=1, verbose_name='Precio del plan')),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('idSucursal', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de la Sucursal')),
                ('nombreSucursal', models.CharField(max_length=30, verbose_name='Nombre del Sucursal')),
                ('direccionSucursal', models.CharField(max_length=50, verbose_name='Dirección de la Sucursal')),
            ],
        ),
        migrations.CreateModel(
            name='TipoFuncionario',
            fields=[
                ('idTipoFuncionario', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID del Tipo Funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('idTipo', models.AutoField(primary_key=True, serialize=False, verbose_name='ID del Tipo de Usuario')),
                ('nombreTipo', models.CharField(max_length=30, verbose_name='Nombre Tipo de Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('idSocio', models.AutoField(primary_key=True, serialize=False, verbose_name='ID del Socio')),
                ('edad', models.IntegerField(null=True, verbose_name='edad del Socio')),
                ('altura', models.IntegerField(null=True, verbose_name='altura del Socio')),
                ('peso', models.IntegerField(null=True, verbose_name='peso del Socio')),
                ('titularPlan', models.CharField(max_length=30, null=True, verbose_name='Titular del Plan')),
                ('direccion', models.CharField(max_length=125, null=True, verbose_name='Direccion')),
                ('comuna', models.CharField(max_length=35, null=True, verbose_name='comuna')),
                ('ciudad', models.CharField(max_length=35, null=True, verbose_name='ciudad')),
                ('gSanguineo', models.CharField(max_length=3, null=True, verbose_name='Grupo sanguineo')),
                ('emergenciacontacto', models.CharField(max_length=35, null=True, verbose_name='Nombre de contacto a llamar en caso d emergencia')),
                ('emergenciacontactoTel', models.CharField(max_length=10, null=True, verbose_name='Telefono de contacto a llamar en caso d emergencia')),
                ('pLesion', models.BooleanField(default=False, verbose_name='Posee lesiones?')),
                ('dLesion', models.CharField(max_length=200, null=True, verbose_name='Descripcion lesiones')),
                ('pEnfer', models.BooleanField(default=False, verbose_name='Posee enfermedades prexistentes?')),
                ('dEnfer', models.CharField(max_length=200, null=True, verbose_name='Descripcion enfermedades prexistentes')),
                ('pDArtic', models.BooleanField(default=False, verbose_name='Posee dolores en las articulaciones?')),
                ('dDArtic', models.CharField(max_length=200, null=True, verbose_name='Descripcion dolores en las articulaciones?')),
                ('pDeporte', models.BooleanField(default=False, verbose_name='Practica algun deporte?')),
                ('dDeporte', models.CharField(max_length=200, null=True, verbose_name='Cuales?')),
                ('nDeporte', models.IntegerField(default=0, null=True, verbose_name='Veces a la semana que hace deportes')),
                ('diabetico', models.BooleanField(default=False, verbose_name='es usted diabetico?')),
                ('asmatico', models.BooleanField(default=False, verbose_name='es usted asmatico?')),
                ('epileptico', models.BooleanField(default=False, verbose_name='es usted epiliptico?')),
                ('fumador', models.BooleanField(default=False, verbose_name='fuma?')),
                ('plan', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='gym.plan')),
                ('sucursal', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='gym.sucursal')),
                ('usuario', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('idReserva', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de Reserva')),
                ('socio', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='gym.socio')),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('idProfesor', models.AutoField(primary_key=True, serialize=False, verbose_name='ID del Profesor')),
                ('fechaIngreso', models.DateField(verbose_name='Fecha de Ingreso')),
                ('fechaContrato', models.DateField(verbose_name='Fecha de Contrato')),
                ('sucursal', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='gym.sucursal')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('idFuncionario', models.AutoField(primary_key=True, serialize=False, verbose_name='ID del Funcionario')),
                ('cargo', models.CharField(max_length=20, verbose_name='Cargo del Funcionario')),
                ('tipo', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='gym.tipofuncionario')),
                ('usuario', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Equipamiento',
            fields=[
                ('idEquipamiento', models.AutoField(primary_key=True, serialize=False, verbose_name='ID del Equipamiento')),
                ('nombreEquipamiento', models.CharField(max_length=30, verbose_name='Nombre del Equipamiento')),
                ('sucursal', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='gym.sucursal')),
            ],
        ),
        migrations.CreateModel(
            name='DeporteProfesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deporte', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='gym.deporte')),
                ('profesor', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='gym.profesor')),
            ],
        ),
        migrations.CreateModel(
            name='CursoReserva',
            fields=[
                ('idCursoReserva', models.AutoField(primary_key=True, serialize=False, verbose_name='ID del curso reserva')),
                ('clase', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='gym.clasecurso')),
                ('curso', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='gym.curso')),
                ('socio', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='gym.socio')),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='deporte',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='gym.deporte'),
        ),
        migrations.AddField(
            model_name='curso',
            name='profesor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='gym.profesor'),
        ),
        migrations.AddField(
            model_name='curso',
            name='sucursal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='gym.sucursal'),
        ),
        migrations.AddField(
            model_name='clasecurso',
            name='curso',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='gym.curso'),
        ),
        migrations.CreateModel(
            name='CanchasReserva',
            fields=[
                ('idCanchareserva', models.AutoField(primary_key=True, serialize=False, verbose_name='ID del cancha reserva')),
                ('cancha', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='gym.cancha')),
                ('reserva', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='gym.reserva')),
            ],
        ),
        migrations.AddField(
            model_name='cancha',
            name='deporte',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='gym.deporte'),
        ),
        migrations.AddField(
            model_name='cancha',
            name='sucursal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='gym.sucursal'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='tipoUsuario',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.SET_DEFAULT, to='gym.tipousuario'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
