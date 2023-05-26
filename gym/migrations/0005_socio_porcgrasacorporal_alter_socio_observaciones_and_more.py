# Generated by Django 4.2.1 on 2023-05-26 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0004_usuario_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='socio',
            name='porcGrasaCorporal',
            field=models.IntegerField(default=0, verbose_name='Porc. Grasa Corporal del Socio'),
        ),
        migrations.AlterField(
            model_name='socio',
            name='observaciones',
            field=models.CharField(max_length=500, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='socio',
            name='plan',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='gym.plan'),
        ),
        migrations.AlterField(
            model_name='socio',
            name='sucursal',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='gym.sucursal'),
        ),
        migrations.AlterField(
            model_name='socio',
            name='titularPlan',
            field=models.CharField(max_length=30, null=True, verbose_name='Titular del Plan'),
        ),
    ]
