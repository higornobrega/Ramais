from django.test import TestCase
from setor.models import Setor
from polo.models import Polo
from horario_funcionamento.models import HorarioFuncionamento
from colaborador.models import Colaborador


class SetorModelTestCase(TestCase):

    def setUp(self) -> None:
        self.colaborador = Colaborador.objects.create(
            matricula="0123456789",
            tipo=1,
            nomeColaborador="Fulano de Tal",
            emailInstitucional="fulano@gmail.com",
            numero="(83)999999999",
            numeroWhatsapp="(83)999999999",
            sexo=1,
            instagram="@fulano",
            linkedin="@fulano",
            natVinc=1,
            cargaHoraria=40,
        )

        self.horario_funcionamento = HorarioFuncionamento.objects.create(
            turno=1, inicioFuncionamento='07:00', finalFuncionamento='08:00')


        self.polo = Polo.objects.create(
            nomeDoPolo='Polo Teste',
            campus='Campus Teste'
        )
        self.setor = Setor.objects.create(
            nomeDoSetor='Setor teste', ramal="(83)999999999", numeroWhatsapp="(83)999999999", bloco="A")

        self.setor.polo.set((self.polo,))
        self.setor.horarioFuncionamento.set((self.horario_funcionamento,))
        self.setor.colaborador.set((self.colaborador,))
        self.colaborador.polo.set((self.polo,))

    def test_setor_de_colaborador(self):
        """É informado todos os dados para registrar setor, ele deve ser registrado"""

        self.assertEqual(self.setor.nomeDoSetor, "Setor teste")
        self.assertEqual(self.setor.ramal,"(83)999999999")
        self.assertEqual(self.setor.numeroWhatsapp,"(83)999999999")
        self.assertEqual(self.setor.polo.get(), self.polo)
        self.assertEqual(self.setor.horarioFuncionamento.get(), self.horario_funcionamento)
        self.assertEqual(self.setor.colaborador.get(), self.colaborador)

