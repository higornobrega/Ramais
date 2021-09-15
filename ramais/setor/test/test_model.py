from django.test import TestCase
from setor.models import Setor

class SetorModelTestCase(TestCase):
    def setUp(self) -> None:
        self.setor = Setor.objects.create(nomeDoSetor = "CEAD")
        
    def test_setor_de_colaborador(self):
        """É informado todos os dados para registrar setor, ele deve ser registrado"""

        self.assertEqual(self.setor.nomeDoSetor, "CEAD") 