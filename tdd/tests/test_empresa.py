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

    def test_add_varios_funcionarios(self):
        funcionario1 = Funcionario("Matheus")
        funcionario2 = Funcionario("Joice")

        self.empresa.adicionar_funcionario(funcionario1)
        self.empresa.adicionar_funcionario(funcionario2)

        self.assertEqual(2, len(self.empresa.funcionarios))

    def test_add_funcionario_null(self):
        with self.assertRaises(ValueError):
            self.empresa.adicionar_funcionario(None)

    def test_add_mesmo_funcionario(self):
        funcionario = Funcionario("Eduardo")

        self.empresa.adicionar_funcionario(funcionario)
        with self.assertRaises(ValueError):
            self.empresa.adicionar_funcionario(funcionario)

    def test_add_projeto_na_empresa(self):
        projeto = Projeto("Projeto Teste")

        self.empresa.adicionar_projeto(projeto)

    def test_add_varios_projetos_na_empresa(self):
        projeto1 = Projeto("Projeto Teste")
        projeto2 = Projeto("Projeto Teste 2")

        self.empresa.adicionar_projeto(projeto1)
        self.empresa.adicionar_projeto(projeto2)

        self.assertEqual(2, len(self.empresa.projetos))

    def test_add_projeto_null(self):
        with self.assertRaises(ValueError):
            self.empresa.adicionar_projeto(None)

    def test_add_mesmo_projeto(self):
        projeto = Projeto("Projeto Teste")

        self.empresa.adicionar_projeto(projeto)

        self.empresa.adicionar_projeto(projeto)
        with self.assertRaises(ValueError):
            self.empresa.adicionar_projeto(projeto)
