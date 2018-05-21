from django.db import models

# Create your models here.


class Vendedor2(models.Model):
    rut = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=10)
    digitoverificador = models.CharField(max_length=1)
    cargo = models.CharField(max_length=50)
    telefono = models.PositiveSmallIntegerField()
    numerodecargas = models.PositiveSmallIntegerField()
    sueldobase = models.PositiveSmallIntegerField()
    fecha_contrato = models.DateField()
