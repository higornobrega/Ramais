from django.test import TestCase
from polo.models import Polo


class PoloModelTestCase(TestCase): 
    def setUp(self):
        self.polo = Polo.objects.create(
            nomeDoPolo = 'Polo Teste',
            endereco = 'Rua teste',
            campus = 'Campus Teste'
        )
    
    def test_cadastrar_polo_com_todos_os_dados(self):
        """É informado todos os dados para registrar Polo e ele é cadastrado"""
        
        self.assertEqual(self.polo.nomeDoPolo, 'Polo Teste')
        self.assertEqual(self.polo.endereco, 'Rua teste')
        self.assertEqual(self.polo.campus, 'Campus Teste')
        