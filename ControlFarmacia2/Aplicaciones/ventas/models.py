from django.db import models

# Create your models here.
TIPO_PAGO = (('Efec', 'Efectivo'), ('Tarj', 'Tarjeta Credito y Debito'), ('Cheq', 'Cheques'))


class Cajero(models.Model):
    vale = models.PositiveSmallIntegerField()
    fechayhora = models.DateTimeField()
    monto = models.PositiveSmallIntegerField()
    nombre_cajero = models.TextField()
    tipo_pago = models.CharField(max_length=4, choices=TIPO_PAGO, default='Efec')
    total_vales = models.PositiveSmallIntegerField()
    pago = models.PositiveSmallIntegerField()
    vuelto = models.PositiveSmallIntegerField()


class Respaldo_cajero(models.Model):
    vale = models.PositiveSmallIntegerField()
    fechayhora = models.DateTimeField()
    monto = models.PositiveSmallIntegerField()
    nombre_cajero = models.TextField()
    tipo_pago = models.CharField(max_length=4, choices=TIPO_PAGO, default='Efec')
    total_vales = models.PositiveSmallIntegerField()
    pago = models.PositiveSmallIntegerField()
    vuelto = models.PositiveSmallIntegerField()


class Vale1(models.Model):
    vale = models.PositiveSmallIntegerField()
    fechayhora = models.DateTimeField()
    codigo = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=100)
    cantidad = models.PositiveSmallIntegerField(default=1)
    precio_venta = models.PositiveSmallIntegerField()
    factor = models.DecimalField(max_digits=5, decimal_places=2)
    conversion = models.FloatField(default=1)
    vendedor = models.PositiveSmallIntegerField()
    total = models.PositiveSmallIntegerField()
    local = models.PositiveSmallIntegerField()
    stock = models.PositiveSmallIntegerField(default=0)
    descuento = models.BooleanField(default=False)
    impresa = models.BooleanField(default=False)


class Vale2(models.Model):
    vale = models.PositiveSmallIntegerField()
    fechayhora = models.DateTimeField()
    codigo = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=100)
    cantidad = models.PositiveSmallIntegerField(default=1)
    precio_venta = models.PositiveSmallIntegerField()
    factor = models.DecimalField(max_digits=5, decimal_places=2)
    conversion = models.FloatField(default=1)
    vendedor = models.PositiveSmallIntegerField()
    total = models.PositiveSmallIntegerField()
    local = models.PositiveSmallIntegerField()
    stock = models.PositiveSmallIntegerField(default=0)
    descuento = models.BooleanField(default=False)
    impresa = models.BooleanField(default=False)


class Vale3(models.Model):
    vale = models.PositiveSmallIntegerField()
    fechayhora = models.DateTimeField()
    codigo = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=100)
    cantidad = models.PositiveSmallIntegerField(default=1)
    precio_venta = models.PositiveSmallIntegerField()
    factor = models.DecimalField(max_digits=5, decimal_places=2)
    conversion = models.FloatField(default=1)
    vendedor = models.PositiveSmallIntegerField()
    total = models.PositiveSmallIntegerField()
    local = models.PositiveSmallIntegerField()
    stock = models.PositiveSmallIntegerField(default=0)
    descuento = models.BooleanField(default=False)
    impresa = models.BooleanField(default=False)


class Vale4(models.Model):
    vale = models.PositiveSmallIntegerField()
    fechayhora = models.DateTimeField()
    codigo = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=100)
    cantidad = models.PositiveSmallIntegerField(default=1)
    precio_venta = models.PositiveSmallIntegerField()
    factor = models.DecimalField(max_digits=5, decimal_places=2)
    conversion = models.FloatField(default=1)
    vendedor = models.PositiveSmallIntegerField()
    total = models.PositiveSmallIntegerField()
    local = models.PositiveSmallIntegerField()
    stock = models.PositiveSmallIntegerField(default=0)
    descuento = models.BooleanField(default=False)
    impresa = models.BooleanField(default=False)


class Vale5(models.Model):
    vale = models.PositiveSmallIntegerField()
    fechayhora = models.DateTimeField()
    codigo = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=100)
    cantidad = models.PositiveSmallIntegerField(default=1)
    precio_venta = models.PositiveSmallIntegerField()
    factor = models.DecimalField(max_digits=5, decimal_places=2)
    conversion = models.FloatField(default=1)
    vendedor = models.PositiveSmallIntegerField()
    total = models.PositiveSmallIntegerField()
    local = models.PositiveSmallIntegerField()
    stock = models.PositiveSmallIntegerField(default=0)
    descuento = models.BooleanField(default=False)
    impresa = models.BooleanField(default=False)


class Respaldo_Vale(models.Model):
    vale = models.PositiveSmallIntegerField()
    fechayhora = models.DateTimeField()
    codigo = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=100)
    cantidad = models.PositiveSmallIntegerField(default=1)
    precio_venta = models.PositiveSmallIntegerField()
    factor = models.DecimalField(max_digits=5, decimal_places=2)
    conversion = models.FloatField(default=1)
    vendedor = models.PositiveSmallIntegerField()
    total = models.PositiveSmallIntegerField()
    local = models.PositiveSmallIntegerField()
    stock = models.PositiveIntegerField(default=0)
    descuento = models.BooleanField(default=False)
    impresa = models.BooleanField(default=False)


class Respaldo_Vale_total(models.Model):
    vale = models.PositiveSmallIntegerField()
    fechayhora = models.DateTimeField()
    codigo = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=100)
    cantidad = models.PositiveSmallIntegerField(default=1)
    precio_venta = models.PositiveSmallIntegerField()
    factor = models.DecimalField(max_digits=5, decimal_places=2)
    conversion = models.FloatField(default=1)
    vendedor = models.PositiveSmallIntegerField()
    total = models.PositiveSmallIntegerField()
    local = models.PositiveSmallIntegerField()
    stock = models.PositiveSmallIntegerField()
    descuento = models.BooleanField(default=False)
    impresa = models.BooleanField(default=False)
