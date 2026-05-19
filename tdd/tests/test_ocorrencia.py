import unittest
from ocorrencia import Ocorrencia
from funcionario import Funcionario
from projeto import Projeto


class TestOcorrencia(unittest.TestCase):

    def setUp(self):
        self.projeto = Projeto("Projeto Teste")
        self.funcionario = Funcionario("Hugo")

    def test_instanciar_ocorrencia_funcionario_nulo(self):
        with self.assertRaises(ValueError):
            Ocorrencia(None, 1, "")

    def test_instanciar_ocorrencia_tipo_funcionario_invalido(self):
        with self.assertRaises(ValueError):
            Ocorrencia(1, 2, "Qualquer resumo")

    def test_instanciar_ocorrencia_sucesso(self):
        ocorrencia = Ocorrencia(self.funcionario, 1, "Resumo da ocorrencia")

        self.assertEqual(id(self.funcionario), id(ocorrencia.responsavel))
        self.assertEqual(1, ocorrencia.chave)
        self.assertEqual("Resumo da ocorrencia", ocorrencia.resumo)

    def test_criar_ocorrencia_funcionario_nao_esta_no_projeto(self):
        with self.assertRaises(ValueError):
            self.projeto.criar_ocorrencia(self.funcionario)

    def test_criar_ocorrencia_funcionario_sucesso(self):
        self.projeto.adicionar_funcionario(self.funcionario)
        ocorrencia = self.projeto.criar_ocorrencia(self.funcionario)

        self.assertEqual(self.funcionario.nome, ocorrencia.responsavel.nome)
