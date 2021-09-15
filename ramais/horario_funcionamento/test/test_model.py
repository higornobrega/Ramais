from django.test import TestCase
from horario_funcionamento.models import HorarioFuncionamento


class HorarioFuncionamentoModelTestCase(TestCase):
    def setUp(self) -> None:
        self.horario_funcionamento = HorarioFuncionamento.objects.create(turno=1, inicioFuncionamento = '07:00', finalFuncionamento = '08:00')

    def test_horario_funcionamento_de_colaborador(self):
        """É informado todos os dados para registrar horário de funcionamento e ele é registrado"""
        self.assertEqual(self.horario_funcionamento.turno, 1)
        self.assertEqual(self.horario_funcionamento.inicioFuncionamento, '07:00')
        self.assertEqual(self.horario_funcionamento.finalFuncionamento, '08:00')