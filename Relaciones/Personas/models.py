from django.db import models

# Create your models here.

class Documento(models.Model):
    tipo = models.CharField(max_length=2, verbose_name='Tipo de documento')

class Persona(models.Model):
    nombre = models.CharField(max_length=10, verbose_name='Nombre')
    apellido = models.CharField(max_length=10, verbose_name='Apellido')
    correo = models.EmailField(verbose_name='Correo electronico')
    fecha_nacimiento = models.DateField( default=False, verbose_name='Fecha de nacimiento')
    tipo_documento = models.ForeignKey(Documento, on_delete=models.PROTECT)

