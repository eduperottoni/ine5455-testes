import unittest
from empresa import Empresa


class TestEmpresa(unittest.TestCase):

    def test_criar_empresa(self):
        empresa = Empresa("Companhia do Código")
        self.assertEqual(empresa.nome, "Companhia do Código")
