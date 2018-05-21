# Generated by Django 2.0.4 on 2018-05-20 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle_facturas',
            name='cantidad',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='detalle_facturas',
            name='codigo',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='detalle_facturas',
            name='conversion',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='detalle_facturas',
            name='descuento',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='detalle_facturas',
            name='factor',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='detalle_facturas',
            name='local',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='detalle_facturas',
            name='nota_credito',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='detalle_facturas',
            name='numero_serie',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='detalle_facturas',
            name='numerofactura',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='detalle_facturas',
            name='precioventa',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='factura',
            name='monto',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='factura',
            name='numerofactura',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='factura',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='facturas.Proveedor'),
        ),
        migrations.AlterField(
            model_name='ingreso_facturas1',
            name='cantidad',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='ingreso_facturas1',
            name='codigo',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='ingreso_facturas1',
            name='conversion',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='ingreso_facturas1',
            name='descuento',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='ingreso_facturas1',
            name='factor',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='ingreso_facturas1',
            name='local',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='ingreso_facturas1',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ingreso_facturas1',
            name='precio_venta',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='ingreso_facturas1',
            name='total',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='ingreso_facturas2',
            name='cantidad',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='ingreso_facturas2',
            name='codigo',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='ingreso_facturas2',
            name='factor',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='ingreso_facturas2',
            name='local',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='ingreso_facturas2',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ingreso_facturas2',
            name='precio_venta',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='ingreso_facturas2',
            name='total',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='ingreso_facturas3',
            name='cantidad',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='ingreso_facturas3',
            name='codigo',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='ingreso_facturas3',
            name='factor',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='ingreso_facturas3',
            name='local',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='ingreso_facturas3',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ingreso_facturas3',
            name='precio_venta',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='ingreso_facturas3',
            name='total',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='ingreso_facturas4',
            name='cantidad',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='ingreso_facturas4',
            name='codigo',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='ingreso_facturas4',
            name='factor',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='ingreso_facturas4',
            name='local',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='ingreso_facturas4',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ingreso_facturas4',
            name='precio_venta',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='ingreso_facturas4',
            name='total',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='ingreso_facturas5',
            name='cantidad',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='ingreso_facturas5',
            name='codigo',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='ingreso_facturas5',
            name='factor',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='ingreso_facturas5',
            name='local',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='ingreso_facturas5',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ingreso_facturas5',
            name='precio_venta',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='ingreso_facturas5',
            name='total',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='direccion',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='fono_empresa',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='fono_vendedor',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='rut',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='vendedor',
            field=models.CharField(max_length=100),
        ),
    ]
