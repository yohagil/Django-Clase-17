from django.db import models

# Create your models here.
class Curso(models.model):
 nombre = models.CharField(max_length=40)
 camada = models.integerfield()

 class Profesor(models.model):
  nombre = models.CharField(max_length=40) 
  apellido = models.CharField(max_length=20)
  email = models.CharField(max_length=40)
  apellido = models.CharField(max_length=30)
  

