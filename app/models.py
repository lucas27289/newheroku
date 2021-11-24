from django.db import models

# Create your models here.
class Dato(models.Model):
    nombre = models.CharField(max_length=50)
    valor = models.IntegerField()