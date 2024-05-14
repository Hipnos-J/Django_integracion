from django.db import models

# Create your models here.
class Tarea(models.Model):
    descripcion = models.CharField(max_length=200)
    eliminada = models.BooleanField(default=False)
    
class SubTarea(models.Model):
    descripcion = models.CharField(max_length=200)
    eliminada = models.BooleanField(default=False)
    tarea = models.ForeignKey('Tarea', on_delete=models.CASCADE, null=False, blank=False)
    
