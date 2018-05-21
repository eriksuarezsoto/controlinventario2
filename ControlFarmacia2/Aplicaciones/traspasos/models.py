from django.db import models

# Create your models here.


class Traspasos_entre_locales(models.Model):
    codigo = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=100)
    preciocompra = models.FloatField()
    precioventa = models.PositiveSmallIntegerField()
    factor = models.FloatField()
    local_origen = models.PositiveSmallIntegerField()
    local_destino = models.PositiveSmallIntegerField()
    numero_vale = models.PositiveSmallIntegerField()
    fecha_traspaso = models.DateTimeField()
    cantidad = models.PositiveSmallIntegerField()
    codigobarra = models.PositiveIntegerField()
    tipo = models.ForeignKey('productos.Tipo2', on_delete=models.DO_NOTHING)
