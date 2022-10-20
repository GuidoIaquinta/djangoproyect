from django.db import models
from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    dni = models.IntegerField()
    alta = models.DateField()

# Create your models here.
