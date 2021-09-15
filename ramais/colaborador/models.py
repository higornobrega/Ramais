from django.db import models
from polo.models import Polo

class Colaborador(models.Model):
    tipo_colaborador = (
        (1,'Professor(a)'),
        (2,'Gerente'),
        (3,'Secretaria(o)'),
    )
    
    sexo_colaborador = (
        (1,'Masculino'),
        (2,'Feminino'),
        (3,'Outro'),
    )
    
    natVinc_colaborador = (
        (1,'Naturalidade vinculo 1'),
        (2,'Naturalidade vinculo 2'),
        (3,'Naturalidade vinculo 3'),
    )
    
    matricula = models.CharField("Matricula", max_length=50)
    tipo = models.IntegerField("Tipo", choices=tipo_colaborador)
    nomeColaborador = models.CharField("Nome", max_length=254)
    emailInstitucional = models.EmailField("Email Intitucional", max_length=254)
    numero = models.CharField("Nome", max_length=21)
    numeroWhatsapp = models.CharField("Nome", max_length=21, blank=True, null=True)
    sexo = models.IntegerField("Sexo", choices=sexo_colaborador)
    instagram = models.CharField("Instagram", max_length=254)
    #setor = models.ManyToManyField(Setor)
    linkedin = models.CharField("Linkedin", max_length=254)
    imagem = models.ImageField("Imagem", upload_to='foto/%d/%m/%y/', blank=True, null=True)
    natVinc = models.IntegerField("Sexo", choices=natVinc_colaborador)
    cargaHoraria = models.IntegerField("CH")
    polo = models.ManyToManyField(Polo)
    #senha = models.CharField("Senha", max_length=254)
    
