import unittest
from ocorrencia import Ocorrencia
from funcionario import Funcionario
from projeto import Projeto


class TestOcorrencia(unittest.TestCase):

    def setUp(self):
        self.projeto = Projeto("Projeto Teste")
        self.funcionario = Funcionario("Hugo")

    def test_criar_ocorrencia_sem_funcionario(self):
        with self.assertRaises(ValueError):
            self.projeto.criar_ocorrencia()

    def test_criar_ocorrencia_funcionario_nao_esta_no_projeto(self):
        with self.assertRaises(ValueError):
            self.projeto.criar_ocorrencia(self.funcionario)

    def test_criar_ocorrencia_funcionario_sucesso(self):
        self.projeto.adicionar_funcionario(self.funcionario)
        ocorrencia = self.projeto.criar_ocorrencia(self.funcionario)

        self.assertEqual(self.funcionario.nome, ocorrencia.responsavel.nome)
