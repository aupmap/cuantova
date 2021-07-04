from django.db import models

class Cuantovaser(models.Model):
    address =models.CharField(max_length=200, default='DEFAULT VALUE')

def __str__(self):
        return self.address


class Form(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30, null=True, blank=True)
    edad = models.CharField(max_length=30)
    inter = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    interpretacion = models.CharField(max_length=3, null=True, blank=True, choices=inter)
    domic = (
        ('yes', 'Sí'),
        ('no', 'No'),
    )
    domicilio = models.CharField(max_length=3, null=True, blank=True, choices=domic)
    calle = models.CharField(max_length=30)
    numero = models.CharField(max_length=10)
    colonia = models.CharField(max_length=45)
    municipio = models.CharField(max_length=30)
    urg = (
        ('yes', 'Sí'),
        ('no', 'No'),
    )
    urgente = models.CharField(max_length=3, null=True, blank=True, choices=urg)
    nombre_2 = models.CharField(max_length=30)
    apellido_2 = models.CharField(max_length=30, null=True, blank=True)
    celular = models.CharField(max_length=11)

def __str__(self):
    return self.nombre