from django.db import models
from endereco.models import Endereco


class Polo(models.Model):
    nomeDoPolo = models.CharField(max_length=200)
    campus = models.CharField(max_length=200)
    endereco = models.ManyToManyField(Endereco, verbose_name="Endereco")


