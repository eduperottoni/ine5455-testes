import unittest
from empresa import Empresa
from funcionario import Funcionario
from projeto import Projeto


class TestEmpresa(unittest.TestCase):

    def setUp(self):
        self.empresa = Empresa("Companhia do Código")

    def test_criar_empresa(self):
        empresa = Empresa("Cia da Equação")
        self.assertEqual(empresa.nome, "Cia da Equação")

    def test_criar_empresa_sem_nome(self):
        with self.assertRaises(TypeError):
            Empresa()

    def test_add_funcionario(self):
        funcionario = Funcionario("Hugo")

        self.empresa.adicionar_funcionario(funcionario)

        self.assertEqual(self.empresa.funcionarios[0].nome, "Hugo")

    def test_add_projeto_na_empresa(self):
        projeto = Projeto("Projeto Teste")

        self.empresa.adicionar_projeto(projeto)
