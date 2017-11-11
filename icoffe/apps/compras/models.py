from django.db import models
from .managers import ComprasManager

class Proveedores(models.Model):
    cod_prov = models.IntegerField(db_column='COD_PROV', primary_key=True)  # Field name made lowercase.
    razon_social = models.CharField(db_column='RAZON_SOCIAL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ruc = models.CharField(db_column='RUC', unique=True, max_length=11, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PROVEEDORES'

class ProveedorStock(models.Model):
    id = models.IntegerField(primary_key=True)
    cod_rpov = models.IntegerField()
    razon_social = models.CharField(max_length=100)
    ruc = models.CharField(max_length=11)
    objects = ComprasManager()