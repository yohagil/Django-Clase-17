from django.db import models

# Create your models here.
class Profesor(models.Model):
  nombre = models.CharField(max_length=40) 
  apellido = models.CharField(max_length=20)
  email = models.CharField(max_length=40)
  profesion = models.CharField(max_length=30)