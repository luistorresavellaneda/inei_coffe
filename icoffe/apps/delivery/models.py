from django.db import models

# Create your models here.
class Pedido(models.Model):
    codigo = models.CharField(max_length=50)
    fecha = models.DateTimeField()
    descripcion = models.TextField()