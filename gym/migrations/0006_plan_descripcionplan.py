# Generated by Django 4.2.1 on 2023-05-26 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0005_socio_porcgrasacorporal_alter_socio_observaciones_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='descripcionPlan',
            field=models.CharField(max_length=500, null=True, verbose_name='Descripcion del Plan'),
        ),
    ]
