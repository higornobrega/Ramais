from django.test import TestCase
from colaborador.models import Colaborador
from polo.models import Polo
from endereco.models import Endereco


class ColaboradorModelTestCase(TestCase):
    def setUp(self) -> None:
        self.endereco = Endereco.objects.create(nomeDaRua='Rua dos Bobos', cep='59360-000', bairro='bairro Test', numeroDaResidencia='numeroDaResidencia test',estado='estado test', cidade='cidade teste', pais='pais teste', pontoDeReferencia='pontoDeReferencia teste', complemento='complemento teste')

        self.polo = Polo.objects.create(
            nomeDoPolo="Polo Teste", campus="Campus Teste"
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
        self.polo.endereco.set((self.endereco,))

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
