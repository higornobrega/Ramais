from django.db import models
from polo.models import Polo
from horario_funcionamento.models import HorarioFuncionamento
from colaborador.models import Colaborador

class Setor(models.Model):
    nomeDoSetor = models.CharField("Nome do Setor", max_length=250)
    ramal = models.CharField("Ramal", max_length=250)
    numeroWhatsapp = models.CharField("Nome", max_length=21, blank=True, null=True)
    bloco = models.CharField('Bloco', max_length=250)
    polo = models.ManyToManyField(Polo, verbose_name="Polo")
    horarioFuncionamento = models.ManyToManyField(HorarioFuncionamento, verbose_name="Horario de Funcionamento")
    colaborador = models.ManyToManyField(Colaborador, verbose_name="Colaborador")