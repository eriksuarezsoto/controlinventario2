from django.db import models

# Create your models here.


class Detalle_facturas(models.Model):
    numerofactura = models.PositiveSmallIntegerField()
    codigo = models.PositiveSmallIntegerField()
    cantidad = models.PositiveSmallIntegerField()
    preciocompra = models.FloatField()
    precioventa = models.PositiveIntegerField()
    conversion = models.PositiveSmallIntegerField()
    factor = models.DecimalField(max_digits=5, decimal_places=2)
    local = models.PositiveSmallIntegerField()
    numero_serie = models.CharField(max_length=20)
    fecha_vencimiento = models.DateField()
    nota_credito = models.PositiveSmallIntegerField()
    descuento = models.FloatField()


class Factura(models.Model):
    numerofactura = models.PositiveIntegerField()
    proveedor = models.ForeignKey('Proveedor', on_delete=models.DO_NOTHING)
    fecha = models.DateField()
    monto = models.PositiveIntegerField()


class Ingreso_facturas1(models.Model):
    codigo = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=100)
    cantidad = models.PositiveSmallIntegerField()
    conversion = models.PositiveSmallIntegerField()
    precio_compra = models.FloatField()
    precio_venta = models.PositiveSmallIntegerField()
    factor = models.DecimalField(max_digits=5, decimal_places=2)
    descuento = models.FloatField()
    total = models.PositiveSmallIntegerField()
    fechayhora = models.DateTimeField()
    stock = models.IntegerField()
    fecha_vencimiento = models.DateTimeField()
    local = models.PositiveSmallIntegerField()


class Ingreso_facturas2(models.Model):
    codigo = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=100)
    cantidad = models.PositiveSmallIntegerField()
    conversion = models.FloatField()
    precio_compra = models.FloatField()
    precio_venta = models.PositiveSmallIntegerField()
    factor = models.DecimalField(max_digits=5, decimal_places=2)
    descuento = models.IntegerField()
    total = models.PositiveSmallIntegerField()
    fechayhora = models.DateTimeField()
    stock = models.IntegerField()
    fecha_vencimiento = models.DateTimeField()
    local = models.PositiveSmallIntegerField()


class Ingreso_facturas3(models.Model):
    codigo = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=100)
    cantidad = models.PositiveSmallIntegerField()
    conversion = models.FloatField()
    precio_compra = models.FloatField()
    precio_venta = models.PositiveSmallIntegerField()
    factor = models.DecimalField(max_digits=5, decimal_places=2)
    descuento = models.IntegerField()
    total = models.PositiveSmallIntegerField()
    fechayhora = models.DateTimeField()
    stock = models.IntegerField()
    fecha_vencimiento = models.DateTimeField()
    local = models.PositiveSmallIntegerField()


class Ingreso_facturas4(models.Model):
    codigo = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=100)
    cantidad = models.PositiveSmallIntegerField()
    conversion = models.FloatField()
    precio_compra = models.FloatField()
    precio_venta = models.PositiveSmallIntegerField()
    factor = models.DecimalField(max_digits=5, decimal_places=2)
    descuento = models.IntegerField()
    total = models.PositiveSmallIntegerField()
    fechayhora = models.DateTimeField()
    stock = models.IntegerField()
    fecha_vencimiento = models.DateTimeField()
    local = models.PositiveSmallIntegerField()


class Ingreso_facturas5(models.Model):
    codigo = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=100)
    cantidad = models.PositiveSmallIntegerField()
    conversion = models.FloatField()
    precio_compra = models.FloatField()
    precio_venta = models.PositiveSmallIntegerField()
    factor = models.DecimalField(max_digits=5, decimal_places=2)
    descuento = models.IntegerField()
    total = models.PositiveSmallIntegerField()
    fechayhora = models.DateTimeField()
    stock = models.IntegerField()
    fecha_vencimiento = models.DateTimeField()
    local = models.PositiveSmallIntegerField()


class Proveedor(models.Model):
    rut = models.PositiveIntegerField(primary_key=True)
    digitoverificador = models.CharField(max_length=1)
    nombre = models.CharField(max_length=100)
    fono_empresa = models.PositiveSmallIntegerField()
    direccion = models.CharField(max_length=100)
    vendedor = models.CharField(max_length=100)
    fono_vendedor = models.PositiveIntegerField()
