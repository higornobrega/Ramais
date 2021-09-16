from django.test import TestCase
from endereco.models import Endereco

class EnderecoModelTestCase(TestCase):
    def setUp(self):
        self.endereco = Endereco.objects.create(nomeDaRua='Rua dos Bobos', cep='59360-000', bairro='bairro Test', numeroDaResidencia='numeroDaResidencia test',estado='estado test', cidade='cidade teste', pais='pais teste', pontoDeReferencia='pontoDeReferencia teste', complemento='complemento teste')

    def test_setor_de_colaborador(self):
        """É informado todos os dados para registrar endereço e ele é registrado"""
        
        self.assertEqual(self.endereco.nomeDaRua, "Rua dos Bobos")
        self.assertEqual(self.endereco.cep, "59360-000")
        self.assertEqual(self.endereco.bairro, "bairro Test")
        self.assertEqual(self.endereco.numeroDaResidencia, "numeroDaResidencia test")
        self.assertEqual(self.endereco.estado, "estado test")
        self.assertEqual(self.endereco.cidade, "cidade teste")
        self.assertEqual(self.endereco.pais, "pais teste")
        self.assertEqual(self.endereco.pontoDeReferencia, "pontoDeReferencia teste")
        self.assertEqual(self.endereco.complemento, "complemento teste")

