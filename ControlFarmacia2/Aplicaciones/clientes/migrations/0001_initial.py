# Generated by Django 2.0.4 on 2018-05-08 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('rut', models.IntegerField(primary_key=True, serialize=False)),
                ('digitoverificador', models.CharField(max_length=1)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Registro_ventas',
            fields=[
                ('rut', models.IntegerField()),
                ('digitoverificador', models.CharField(max_length=1)),
                ('vale', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
