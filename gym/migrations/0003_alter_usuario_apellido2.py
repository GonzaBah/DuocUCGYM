# Generated by Django 4.2.1 on 2023-06-02 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0002_alter_usuario_apellido2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='apellido2',
            field=models.CharField(max_length=30, null=True, verbose_name='Segundo apellido del Usuario'),
        ),
    ]
