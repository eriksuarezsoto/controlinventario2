# Generated by Django 2.0.4 on 2018-05-08 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Composicion',
            fields=[
                ('codigodroga', models.IntegerField(primary_key=True, serialize=False)),
                ('cantidad_una_dosis', models.IntegerField()),
                ('dosis_por_envase', models.IntegerField()),
                ('componente', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Drogas',
            fields=[
                ('codigodroga', models.IntegerField(primary_key=True, serialize=False)),
                ('nombredroga', models.CharField(max_length=50)),
                ('refrigerado', models.BooleanField()),
                ('controlado', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='barra',
            name='id',
        ),
        migrations.RemoveField(
            model_name='eliminados',
            name='id',
        ),
        migrations.RemoveField(
            model_name='listado_productos',
            name='id',
        ),
        migrations.AlterField(
            model_name='barra',
            name='barra',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='eliminados',
            name='codigo',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='listado_productos',
            name='codigo',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='listado_productos',
            name='codigodroga',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='productos.Drogas'),
        ),
    ]
