from django.db import models

# Create your models here.
class Profesor(models.model):
  nombre = models.CharField(max_length=40) 
  apellido = models.CharField(max_length=20)
  email = models.CharField(max_length=40)
  apellido = models.CharField(max_length=30)