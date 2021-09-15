from django.test import TestCase
from colaborador.models import Colaborador
from polo.models import Polo


class ColaboradorModelTestCase(TestCase):
    def setUp(self) -> None:
        self.polo = Polo.objects.create(
            nomeDoPolo="Polo Teste", endereco="Rua teste", campus="Campus Teste"
        )

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

        self.colaborador.polo.set((self.polo,))

    def test_cadastro_de_colaborador(self):
        """É informado todos os dados para registrar colaborador e ele é registrado"""

        self.assertEqual(self.colaborador.matricula, "0123456789")
        self.assertEqual(self.colaborador.tipo, 1)
        self.assertEqual(self.colaborador.nomeColaborador, "Fulano de Tal")
        self.assertEqual(
            self.colaborador.emailInstitucional,
            "fulano@gmail.com",
        )
        self.assertEqual(self.colaborador.numero, "(83)999999999")
        self.assertEqual(self.colaborador.sexo, 1)
        self.assertEqual(self.colaborador.instagram, "@fulano")
        self.assertEqual(self.colaborador.linkedin, "@fulano")
        self.assertEqual(self.colaborador.natVinc, 1)
        self.assertEqual(self.colaborador.cargaHoraria, 40)
        self.assertEqual(self.colaborador.polo.get(), self.polo)
