import unittest
from ocorrencia import Ocorrencia
from funcionario import Funcionario
from projeto import Projeto


class TestOcorrencia(unittest.TestCase):

    def setUp(self):
        self.projeto = Projeto("Projeto Teste")
        self.funcionario = Funcionario("Hugo")
        self.projeto.adicionar_funcionario(self.funcionario)

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
        self.assertEqual(False, ocorrencia.estado)

    def test_criar_ocorrencia_funcionario_nao_esta_no_projeto(self):
        joao = Funcionario("Joao")
        with self.assertRaises(ValueError):
            self.projeto.criar_ocorrencia(joao, "qualquer descricao")

    def test_criar_ocorrencia_sucesso(self):
        ocorrencia = self.projeto.criar_ocorrencia(self.funcionario, "Qualquer resumo")

        self.assertEqual(self.funcionario.nome, ocorrencia.responsavel.nome)
        self.assertEqual(1, ocorrencia.chave)
        self.assertEqual("Qualquer resumo", ocorrencia.resumo)
        self.assertEqual(1, len(self.projeto.ocorrencias))

    def test_criar_ocorrencia_resumo_vazio(self):
        with self.assertRaises(ValueError):
            self.projeto.criar_ocorrencia(self.funcionario, "")

    def test_criar_ocorrencia_resumo_poucas_letras(self):
        with self.assertRaises(ValueError):
            self.projeto.criar_ocorrencia(self.funcionario, "nada")

    def test_criar_ocorrencia_gera_chave_correta(self):
        ocorrencia1 = self.projeto.criar_ocorrencia(self.funcionario, "Qualquer resumo")

        self.assertEqual(1, ocorrencia1.chave)

        ocorrencia2 = self.projeto.criar_ocorrencia(
            self.funcionario, "Qualquer outro resumo"
        )

        self.assertEqual(2, ocorrencia2.chave)

    def test_fechar_ocorrencia(self):
        ocorrencia = self.projeto.criar_ocorrencia(self.funcionario, "Qualquer resumo")
        ocorrencia.fechar()

        self.assertEqual(True, ocorrencia.estado)

    # def test_mudar_funcionario(self):
    #     ocorrencia1 = self.projeto.criar_ocorrencia(self.funcionario, "Qualquer resumo")
    #     jorge = Funcionario("Jorge")
    #     self.projeto.mudar_funcionario(1, jorge)

    # def test_mudar_funcionario_ocorrencia_fechada(self):
    #     ocorrencia1 = self.projeto.criar_ocorrencia(self.funcionario, "Qualquer resumo")
    #     ocorrencia1.estado = True

    # def test_mudar_funcionario_ocorrencia_invalida(self):

    # def test_mudar_funcionario_nao_esta_no_projeto(self):
