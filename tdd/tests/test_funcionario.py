import unittest
from funcionario import Funcionario
from ocorrencia import Ocorrencia, TipoOcorrencia, PrioridadeOcorrencia


class TestFuncionario(unittest.TestCase):

    def setUp(self):
        self.funcionario = Funcionario("Eduardo")
        self.ocorrencia_aberta = Ocorrencia(
            self.funcionario, 1, "Resumo qualquer", TipoOcorrencia.TAREFA, PrioridadeOcorrencia.ALTA
        )
        self.ocorrencia_fechada = Ocorrencia(
            self.funcionario, 2, "Resumo qualquer", TipoOcorrencia.TAREFA, PrioridadeOcorrencia.ALTA
        )
        self.ocorrencia_fechada.fechar()

    def test_criar_funcionario(self):
        funcionario = Funcionario("Eduardo")
        self.assertEqual("Eduardo", funcionario.nome)

    def test_criar_funcionario_sem_nome(self):
        with self.assertRaises(TypeError):
            _ = Funcionario()

    def test_ocorrencias_abertas(self):
        self.funcionario.adicionar_ocorrencia(self.ocorrencia_aberta)
        self.funcionario.adicionar_ocorrencia(self.ocorrencia_fechada)
        self.funcionario.adicionar_ocorrencia(self.ocorrencia_aberta)

        self.assertEqual(2, self.funcionario.ocorrencias_abertas())
