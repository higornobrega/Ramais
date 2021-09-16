from django.test import TestCase
from polo.models import Polo
from endereco.models import Endereco
class PoloModelTestCase(TestCase): 
    def setUp(self) -> None:
        self.endereco = Endereco.objects.create(nomeDaRua='Rua dos Bobos', cep='59360-000', bairro='bairro Test', numeroDaResidencia='numeroDaResidencia test',estado='estado test', cidade='cidade teste', pais='pais teste', pontoDeReferencia='pontoDeReferencia teste', complemento='complemento teste')


        self.polo = Polo.objects.create(
            nomeDoPolo = 'Polo Teste',
            campus = 'Campus Teste'
        )

        self.polo.endereco.set((self.endereco,))

    
    def test_cadastrar_polo_com_todos_os_dados(self):
        """É informado todos os dados para registrar Polo e ele é cadastrado"""
        
        self.assertEqual(self.polo.nomeDoPolo, 'Polo Teste')
        self.assertEqual(self.polo.campus, 'Campus Teste')
        self.assertEqual(self.polo.endereco.get(), self.endereco)

        