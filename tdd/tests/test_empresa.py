import unittest
from empresa import Empresa
from funcionario import Funcionario


class TestEmpresa(unittest.TestCase):

    def test_criar_empresa(self):
        empresa = Empresa("Companhia do Código")
        self.assertEqual(empresa.nome, "Companhia do Código")

    def test_criar_empresa_sem_nome(self):
        with self.assertRaises(TypeError):
            Empresa()

    def test_add_funcionario(self):
        empresa = Empresa("Companhia do Código")
        funcionario = Funcionario("Hugo")

        empresa.adicionar_funcionario(funcionario)

        self.assertEqual(empresa.funcionarios[0].nome, "Hugo")
