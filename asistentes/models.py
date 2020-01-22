from django.db import models

class Rol(models.Model):
    nombre_rol = models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.nombre_rol

class Participantes(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100,blank=True,null=True)
    email = models.CharField(max_length=100)
    rol = models.ForeignKey(Rol,on_delete=models.SET_NULL,null=True,blank=True)
    fecha_registro = models.DateField(blank=True,null=True)
    
    def __str__(self):
        return self.email

class Asistencia(models.Model):
    dia_uno = models.DateField(blank=True,null=True)
    dia_dos = models.DateField(blank=True,null=True)
    dia_tres = models.DateField(blank=True,null=True)
    participante = models.ForeignKey(Participantes,on_delete=models.SET_NULL,null=True)

class TemasRecursos(models.Model):
    nombre_tema = models.CharField(max_length=300,blank=True,null=True)
    
    def __str__(self):
        return self.nombre_tema

class Recursos(models.Model):
    nombre = models.CharField(max_length=300,blank=True,null=True)
    informacion_recurso = models.CharField(max_length=300,blank=True,null=True)
    tema = models.ForeignKey(TemasRecursos,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.nombre