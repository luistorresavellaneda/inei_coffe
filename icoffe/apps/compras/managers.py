from django.db import models

class ComprasManager(models.Manager):
    def all(self):
        query = self.raw('select 1')
        return query

    def detalle(self, cod_prov):
        query = self.raw('select 1')
        return query