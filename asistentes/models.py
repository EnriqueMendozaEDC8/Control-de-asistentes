from django.db import models

class Participantes(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100,blank=True,null=True)
    email = models.CharField(max_length=100)
    fecha_registro = models.DateField(blank=True,null=True)

class Asistencia(models.Model):
    dia_uno = models.DateField(blank=True,null=True)
    dia_dos = models.DateField(blank=True,null=True)
    dia_tres = models.DateField(blank=True,null=True)
    participante = models.ForeignKey(Participantes,on_delete=models.SET_NULL,null=True)
