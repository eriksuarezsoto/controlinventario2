from django.db import models


class Tipo2(models.Model):
    tipo_numero = models.PositiveSmallIntegerField()
    tipo_nombre = models.CharField(max_length=100)


class Eliminados2(models.Model):
    fecha = models.DateTimeField()
    codigo = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=100)
    local = models.PositiveSmallIntegerField()


class Inventario2(models.Model):
    local = models.PositiveSmallIntegerField()
    codigo = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=100)
    precio_compra = models.IntegerField()
    precio_venta = models.PositiveSmallIntegerField()
    stock_computador = models.IntegerField()
    stock_actual = models.IntegerField()
    fecha_inventario = models.DateTimeField()
    diferencia_inventario = models.IntegerField()


class Proveedor2(models.Model):
    proveedor = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.PositiveIntegerField()
    vendedor = models.CharField(max_length=100)


class Laboratorio2(models.Model):
    laboratorio = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.PositiveIntegerField()
    vendedor = models.CharField(max_length=100)


class Barra2(models.Model):
    barra = models.PositiveIntegerField()
    codigoproducto = models.ForeignKey('Listado_productos2',
                                       null=True, on_delete=models.SET_NULL)
    laboratorio = models.ForeignKey('Laboratorio2',
                                    null=True, on_delete=models.SET_NULL)


class Listado_productos2(models.Model):
    codigo = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=100)
    codigo_barra = models.PositiveIntegerField()
    preciocompra = models.DecimalField(max_digits=10, decimal_places=2)
    fechacreacion = models.DateTimeField()
    precioventa = models.PositiveSmallIntegerField()
    laboratorio = models.ForeignKey('Laboratorio2', on_delete=models.DO_NOTHING)
    precioventa = models.PositiveSmallIntegerField()
    conversion = models.PositiveSmallIntegerField()
    factor = models.DecimalField(max_digits=5, decimal_places=2)
    pedido = models.PositiveSmallIntegerField()
    tipo = models.ForeignKey('Tipo2', on_delete=models.CASCADE)
    ultimo_proveedor = models.ForeignKey('Proveedor2',
                                         on_delete=models.DO_NOTHING)
    eliminado = models.BooleanField(default=False)
    stock = models.IntegerField()
    fecha_ultima_compra = models.DateField()
    faltas = models.BooleanField()
    tipo = models.ForeignKey('Tipo2', on_delete=models.DO_NOTHING)
    eliminado = models.BooleanField(default=False)
    stock_minimo = models.PositiveSmallIntegerField()
    stock_maximo = models.PositiveSmallIntegerField()
    bioequivalente = models.BooleanField(default=False)
    inventariado = models.BooleanField(default=False)
    fecha_inventario = models.DateTimeField()
    controlado = models.BooleanField(default=False)
    refrigerado = models.BooleanField(default=False)
    composicion = models.ForeignKey('Composicion2', on_delete=models.DO_NOTHING)
    codigodroga = models.ForeignKey('Drogas2', null=True,
                                    blank=True, on_delete=models.DO_NOTHING)


class Drogas2(models.Model):
    codigodroga = models.PositiveSmallIntegerField()
    nombredroga = models.CharField(max_length=50)
    refrigerado = models.BooleanField(default=False)
    controlado = models.BooleanField(default=False)


class Composicion2(models.Model):
    codigodroga = models.ForeignKey('Drogas2', on_delete=models.DO_NOTHING)
    cantidad_una_dosis = models.PositiveSmallIntegerField()
    dosis_por_envase = models.PositiveSmallIntegerField()
    componente = models.PositiveSmallIntegerField()


class Distribuidora2(models.Model):
    codigo = models.ForeignKey('Listado_productos2',
                               on_delete=models.DO_NOTHING)
    proveedor = models.ForeignKey('Proveedor2', on_delete=models.DO_NOTHING)
    codigo_proveedor = models.PositiveSmallIntegerField()
