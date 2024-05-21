from django.db import models

# Create your models here.
class Projeto(models.Model):
    nome = models.CharField(max_length=260)
    categoria_premiacao = models.CharField(max_length=90)
    escola = models.CharField(max_length=110)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    ano = models.CharField(max_length=10)

