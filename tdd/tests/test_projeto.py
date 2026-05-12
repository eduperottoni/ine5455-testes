import unittest
from projeto import Projeto
from funcionario import Funcionario


class TestProjeto(unittest.TestCase):

    def setUp(self):
        self.projeto = Projeto("Projeto Teste")

    def test_criar_projeto(self):
        projeto = Projeto("Projeto Teste")
        self.assertEqual(projeto.nome, "Projeto Teste")

    def test_criar_projeto_sem_nome(self):
        with self.assertRaises(TypeError):
            _ = Projeto()

    def test_add_funcionario_no_projeto(self):
        funcionario = Funcionario("Eduardo")

        self.projeto.adicionar_funcionario(funcionario)
        assert self.projeto.funcionarios[0].nome == "Eduardo"

    def test_add_varios_funcionarios_no_projeto(self):
        funcionario1 = Funcionario("Matheus")
        funcionario2 = Funcionario("Joice")

        self.projeto.adicionar_funcionario(funcionario1)
        self.projeto.adicionar_funcionario(funcionario2)

        assert self.projeto.funcionarios[0].nome == "Matheus"
        assert self.projeto.funcionarios[1].nome == "Joice"

    def test_add_funcionario_null(self):

        with self.assertRaises(ValueError):
            self.projeto.adicionar_funcionario(None)

    def test_add_mesmo_funcionario_em_diferentes_projetos(self):
        projeto1 = Projeto("Projeto Teste")
        projeto2 = Projeto("Projeto Teste 2")

        projeto1.adicionar_funcionario(Funcionario("Eduardo"))
        projeto2.adicionar_funcionario(Funcionario("Eduardo"))

        assert len(projeto1.funcionarios) == 1
        assert len(projeto2.funcionarios) == 1
        assert projeto1.funcionarios[0].nome == "Eduardo"
        assert projeto2.funcionarios[0].nome == "Eduardo"

    def test_add_mesmo_funcionario_em_mesmo_projeto(self):

        self.projeto.adicionar_funcionario(Funcionario("Eduardo"))

        with self.assertRaises(ValueError):
            self.projeto.adicionar_funcionario(Funcionario("Eduardo"))

        assert len(self.projeto.funcionarios) == 1
        assert self.projeto.funcionarios[0].nome == "Eduardo"
