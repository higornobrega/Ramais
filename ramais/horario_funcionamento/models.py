from django.db import models

class HorarioFuncionamento(models.Model):
    turno_horario_funcionamento = (
        (1, 'Matutino'),
        (2, 'Vespertino'),
        (3, 'Noturno')
    )
    turno = models.IntegerField('Turno', choices=turno_horario_funcionamento)
    inicioFuncionamento = models.TimeField()
    finalFuncionamento = models.TimeField()