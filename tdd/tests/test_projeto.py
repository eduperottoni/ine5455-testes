import unittest
from projeto import Projeto
from funcionario import Funcionario


class TestProjeto(unittest.TestCase):

    def setUp(self):
        self.projeto = Projeto("Projeto Teste")

    def test_criar_projeto(self):
        projeto = Projeto("Projeto Teste")
        self.assertEqual("Projeto Teste", projeto.nome)

    def test_criar_projeto_sem_nome(self):
        with self.assertRaises(TypeError):
            _ = Projeto()

    def test_add_funcionario_no_projeto(self):
        funcionario = Funcionario("Eduardo")

        self.projeto.adicionar_funcionario(funcionario)
        self.assertEqual("Eduardo", self.projeto.funcionarios[0].nome)

    def test_add_varios_funcionarios_no_projeto(self):
        funcionario1 = Funcionario("Matheus")
        funcionario2 = Funcionario("Joice")

        self.projeto.adicionar_funcionario(funcionario1)
        self.projeto.adicionar_funcionario(funcionario2)

        self.assertEqual("Matheus", self.projeto.funcionarios[0].nome)
        self.assertEqual("Joice", self.projeto.funcionarios[1].nome)

    def test_add_funcionario_null(self):

        with self.assertRaises(ValueError):
            self.projeto.adicionar_funcionario(None)

    def test_add_mesmo_funcionario_em_diferentes_projetos(self):
        projeto1 = Projeto("Projeto Teste")
        projeto2 = Projeto("Projeto Teste 2")

        projeto1.adicionar_funcionario(Funcionario("Eduardo"))
        projeto2.adicionar_funcionario(Funcionario("Eduardo"))

        self.assertEqual(1, len(projeto1.funcionarios))
        self.assertEqual(1, len(projeto2.funcionarios))
        self.assertEqual("Eduardo", projeto1.funcionarios[0].nome)
        self.assertEqual("Eduardo", projeto2.funcionarios[0].nome)

    def test_add_mesmo_funcionario_em_mesmo_projeto(self):

        self.projeto.adicionar_funcionario(Funcionario("Eduardo"))

        with self.assertRaises(ValueError):
            self.projeto.adicionar_funcionario(Funcionario("Eduardo"))

        self.assertEqual(1, len(self.projeto.funcionarios))
        self.assertEqual("Eduardo", self.projeto.funcionarios[0].nome)
