from django.db import models

class Polo(models.Model):
    nomeDoPolo = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    campus = models.CharField(max_length=200)

