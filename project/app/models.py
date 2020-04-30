from django.db import models

# Create your models here.
class produtos(models.Model):
    nome       = models.CharField(max_length=100,blank=False)
    cod_barras = models.CharField(max_length=20,blank=False)
    valor      = models.DecimalField(max_digits=10, decimal_places=2)