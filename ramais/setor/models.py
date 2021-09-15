from django.db import models

class Setor(models.Model):
    nomeDoSetor = models.CharField("Nome do Setor", max_length=250)