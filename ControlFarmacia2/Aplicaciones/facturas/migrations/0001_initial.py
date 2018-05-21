# Generated by Django 2.0.4 on 2018-05-08 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle_facturas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numerofactura', models.IntegerField()),
                ('codigo', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('preciocompra', models.FloatField()),
                ('precioventa', models.IntegerField()),
                ('conversion', models.FloatField()),
                ('factor', models.FloatField()),
                ('local', models.IntegerField()),
                ('numero_serie', models.TextField()),
                ('fecha_vencimiento', models.DateField()),
                ('nota_credito', models.IntegerField()),
                ('descuento', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numerofactura', models.IntegerField()),
                ('proveedor', models.IntegerField()),
                ('fecha', models.DateField()),
                ('monto', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ingreso_facturas1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('nombre', models.TextField()),
                ('cantidad', models.IntegerField()),
                ('conversion', models.FloatField()),
                ('precio_compra', models.FloatField()),
                ('precio_venta', models.IntegerField()),
                ('factor', models.FloatField()),
                ('descuento', models.IntegerField()),
                ('total', models.IntegerField()),
                ('fechayhora', models.DateTimeField()),
                ('stock', models.IntegerField()),
                ('fecha_vencimiento', models.DateTimeField()),
                ('local', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ingreso_facturas2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('nombre', models.TextField()),
                ('cantidad', models.IntegerField()),
                ('conversion', models.FloatField()),
                ('precio_compra', models.FloatField()),
                ('precio_venta', models.IntegerField()),
                ('factor', models.FloatField()),
                ('descuento', models.IntegerField()),
                ('total', models.IntegerField()),
                ('fechayhora', models.DateTimeField()),
                ('stock', models.IntegerField()),
                ('fecha_vencimiento', models.DateTimeField()),
                ('local', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ingreso_facturas3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('nombre', models.TextField()),
                ('cantidad', models.IntegerField()),
                ('conversion', models.FloatField()),
                ('precio_compra', models.FloatField()),
                ('precio_venta', models.IntegerField()),
                ('factor', models.FloatField()),
                ('descuento', models.IntegerField()),
                ('total', models.IntegerField()),
                ('fechayhora', models.DateTimeField()),
                ('stock', models.IntegerField()),
                ('fecha_vencimiento', models.DateTimeField()),
                ('local', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ingreso_facturas4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('nombre', models.TextField()),
                ('cantidad', models.IntegerField()),
                ('conversion', models.FloatField()),
                ('precio_compra', models.FloatField()),
                ('precio_venta', models.IntegerField()),
                ('factor', models.FloatField()),
                ('descuento', models.IntegerField()),
                ('total', models.IntegerField()),
                ('fechayhora', models.DateTimeField()),
                ('stock', models.IntegerField()),
                ('fecha_vencimiento', models.DateTimeField()),
                ('local', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ingreso_facturas5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('nombre', models.TextField()),
                ('cantidad', models.IntegerField()),
                ('conversion', models.FloatField()),
                ('precio_compra', models.FloatField()),
                ('precio_venta', models.IntegerField()),
                ('factor', models.FloatField()),
                ('descuento', models.IntegerField()),
                ('total', models.IntegerField()),
                ('fechayhora', models.DateTimeField()),
                ('stock', models.IntegerField()),
                ('fecha_vencimiento', models.DateTimeField()),
                ('local', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('rut', models.IntegerField(primary_key=True, serialize=False)),
                ('digitoverificador', models.CharField(max_length=1)),
                ('nombre', models.TextField()),
                ('fono_empresa', models.IntegerField()),
                ('direccion', models.TextField()),
                ('vendedor', models.TextField()),
                ('fono_vendedor', models.IntegerField()),
            ],
        ),
    ]
