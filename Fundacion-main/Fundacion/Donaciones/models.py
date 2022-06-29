from django.db import models

# Create your models here.
class Donaciones(models.Model):
    nombre = models.CharField(max_length=20)
    apellido_pat = models.CharField(max_length=50)
    apellido_mat = models.CharField(max_length=50)
    monto = models.CharField(max_length=10)
    
    def __str__(self):
        return self.nombre
