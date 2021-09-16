from django.db import models

class Endereco(models.Model):
    nomeDaRua = models.CharField(max_length=250) 
    cep = models.CharField(max_length=250) 
    bairro = models.CharField(max_length=250) 
    numeroDaResidencia = models.CharField(max_length=250, blank=True, null=True) 
    estado = models.CharField(max_length=250) 
    cidade = models.CharField(max_length=250) 
    pais = models.CharField(max_length=250) 
    pontoDeReferencia = models.CharField(max_length=250) 
    complemento = models.CharField(max_length=250)