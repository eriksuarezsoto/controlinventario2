from django.db import models

# Create your models here.


class Cajeros2(models.Model):
    nombre = models.CharField(max_length=100)
    numero_cajero = models.PositiveSmallIntegerField()


class Gastos2(models.Model):
    numero_gasto = models.PositiveSmallIntegerField()
    gasto = models.CharField(max_length=100)


class Resumen_gastos2(models.Model):
    fecha = models.DateField()
    numero_gasto = models.PositiveSmallIntegerField()
    gasto = models.PositiveSmallIntegerField()


class Cierres2(models.Model):
    fechayhora_inicio = models.DateTimeField()
    fechayhora_termino = models.DateTimeField()
    vale_inicio = models.PositiveSmallIntegerField()
    vale_termino = models.PositiveSmallIntegerField()
    total_suma_ventas = models.PositiveSmallIntegerField()
    local = models.PositiveSmallIntegerField()
    total_dinero_en_caja = models.PositiveSmallIntegerField()
    total_gastos = models.PositiveSmallIntegerField()
    fondo_inicio = models.PositiveSmallIntegerField()
    tarjetas_credito = models.PositiveSmallIntegerField()
    tarjetas_debito = models.PositiveSmallIntegerField()
    dinerosextras1 = models.PositiveSmallIntegerField()
    dinerosextras2 = models.PositiveSmallIntegerField()
    dinerosextras3 = models.PositiveSmallIntegerField()
    dinerosextras4 = models.PositiveSmallIntegerField()
    bip_inicio = models.PositiveSmallIntegerField()
    bip_salida = models.PositiveSmallIntegerField()
    telefono_entrada = models.PositiveSmallIntegerField()
    telefono_salida = models.PositiveSmallIntegerField()
    celular_entrada = models.PositiveSmallIntegerField()
    celular_salida = models.PositiveSmallIntegerField()
    numero_cierre = models.PositiveSmallIntegerField()
    cajero = models.ForeignKey('Cajeros2', on_delete=models.DO_NOTHING)
    suma_entradas = models.PositiveSmallIntegerField()
    suma_salidas = models.PositiveSmallIntegerField()
    diferencia_caja = models.PositiveSmallIntegerField()
    boleta_sii_inicial = models.PositiveSmallIntegerField()
    boleta_sii_final = models.PositiveSmallIntegerField()
    suma_boletas_sii = models.PositiveSmallIntegerField()


class Detalle_gastos2(models.Model):
    numero_cierre = models.PositiveSmallIntegerField()
    gasto = models.TextField()
    monto = models.TextField()
    numero_gasto = models.ForeignKey('Gastos2', on_delete=models.DO_NOTHING)
    fechayhora = models.DateTimeField()
