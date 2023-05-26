# Generated by Django 4.2.1 on 2023-05-26 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0002_alter_deporteprofesor_deporte_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='apellido2',
            field=models.CharField(max_length=30, null=True, verbose_name='Segundo apellido del Usuario'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fechaNacimiento',
            field=models.DateField(null=True, verbose_name='Fecha de Nacimiento'),
        ),
    ]