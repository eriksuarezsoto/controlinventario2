from django.db import models

# Create your models here.


class Ventas_mensuales2(models.Model):
    mes = models.PositiveSmallIntegerField()
    año = models.PositiveSmallIntegerField()
    venta = models.PositiveSmallIntegerField()
    ganancia = models.SmallIntegerField()
    inventario = models.IntegerField()


class Resumen_vendedores2(models.Model):
    mes = models.PositiveSmallIntegerField()
    año = models.PositiveSmallIntegerField()
    vendedor = models.ForeignKey('vendedores.Vendedor2', on_delete=models.CASCADE)
    venta = models.PositiveSmallIntegerField()
    sueldo = models.PositiveSmallIntegerField()
    cargas_familiares = models.PositiveSmallIntegerField()
    dias_trabajados = models.PositiveSmallIntegerField()


class Datos_local2(models.Model):
    numero_local = models.PositiveSmallIntegerField()
    direccion = models.CharField(max_length=100)
    representante = models.CharField(max_length=100)
    telefono = models.PositiveSmallIntegerField()
    comuna = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    nombre_farmacia = models.CharField(max_length=150)
    mensaje = models.CharField(max_length=200)


class Ultima_boleta2(models.Model):
    fecha = models.DateTimeField()
    numero_boleta = models.PositiveSmallIntegerField()


class Password2(models.Model):
    local = models.PositiveSmallIntegerField()
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    password3 = models.CharField(max_length=100)
    fecha_password1 = models.DateField()
    fecha_password2 = models.DateField()
    fecha_password3 = models.DateField()


class Observaciones2(models.Model):
    fecha = models.DateTimeField()
    proceso = models.CharField(max_length=100)
    codigo_antiguo = models.PositiveSmallIntegerField()
    codigo_nuevo = models.PositiveSmallIntegerField()
    nombre_antiguo = models.CharField(max_length=50)
    nombre_nuevo = models.CharField(max_length=50)
    precio_antiguo = models.PositiveSmallIntegerField()
    precio_nuevo = models.PositiveSmallIntegerField()
    local = models.PositiveSmallIntegerField()
    observacion = models.CharField(max_length=100)
