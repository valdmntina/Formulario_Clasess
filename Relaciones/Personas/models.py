from django.db import models

# Create your models here.

class Documento(models.Model):
    tipo = models.CharField(max_length=2)

class Persona(models.Model):
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=10)
    correo = models.EmailField()
    fecha_nacimiento = models.DateField()
    tipo_documento = models.ForeignKey(Documento, on_delete=models.PROTECT)

