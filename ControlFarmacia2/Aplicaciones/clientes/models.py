from django.db import models
# from datetime import datetime


class Clientes2(models.Model):
    rut = models.PositiveIntegerField(primary_key=True, null=False, default=0)
    digitoverificador = models.CharField(max_length=1, default=0)
    nombres = models.CharField(max_length=100, null=False, default='')
    apellidos = models.CharField(max_length=100, null=False, default='')
    direccion = models.CharField(max_length=100, default='')
    correo = models.EmailField(default='')
    telefono = models.PositiveSmallIntegerField(default=0)
    SEXOS = (('F', 'Femenino'), ('M', 'Masculino'))
    fechacreacion = models.DateField(blank=True, auto_now_add=True)
    Sexo = models.CharField(max_length=1, choices=SEXOS, default='F')


def NombreCompleto(self):
        cadena = '{0} {1}'
        return cadena.format(self.nombres, self.apellidos)


def __str__(self):
        return self.NombreCompleto()


class Registro_ventas2(models.Model):
    rut = models.ForeignKey('Clientes2',
                            on_delete=models.DO_NOTHING)
    vale = models.IntegerField(default=0)

    def __str__(self):
        return '{0} {1}'.format(self.rut, self.vale)


class Contactos(models.Model):
    rut = models.IntegerField(),
    nombres = models.CharField(max_length=100),
    apellidos = models.CharField(max_length=100),
    telefono = models.IntegerField(),
    email = models.EmailField(),
    direccion = models. CharField(max_length=100),
    mensaje = models.CharField(max_length=500),
    fechayhora = models.DateTimeField()
