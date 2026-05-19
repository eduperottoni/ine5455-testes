import unittest
from ocorrencia import Ocorrencia, TipoOcorrencia, PrioridadeOcorrencia
from funcionario import Funcionario
from projeto import Projeto


class TestOcorrencia(unittest.TestCase):

    def setUp(self):
        self.projeto = Projeto("Projeto Teste")
        self.hugo = Funcionario("Hugo")
        self.projeto.adicionar_funcionario(self.hugo)

        self.ocorrencia = self.projeto.criar_ocorrencia(
            self.hugo,
            "Qualquer resumo",
            TipoOcorrencia.TAREFA,
            PrioridadeOcorrencia.ALTA,
        )

    def test_instanciar_ocorrencia_funcionario_nulo(self):
        with self.assertRaises(ValueError):
            Ocorrencia(None, 1, "", TipoOcorrencia.TAREFA, PrioridadeOcorrencia.ALTA)

    def test_instanciar_ocorrencia_tipo_funcionario_invalido(self):
        with self.assertRaises(ValueError):
            Ocorrencia(
                1,
                2,
                "Qualquer resumo",
                TipoOcorrencia.TAREFA,
                PrioridadeOcorrencia.ALTA,
            )

    def test_instanciar_ocorrencia_sucesso(self):
        ocorrencia = Ocorrencia(
            self.hugo,
            1,
            "Resumo da ocorrencia",
            TipoOcorrencia.TAREFA,
            PrioridadeOcorrencia.ALTA,
        )

        self.assertEqual(id(self.hugo), id(ocorrencia.responsavel))
        self.assertEqual(1, ocorrencia.chave)
        self.assertEqual("Resumo da ocorrencia", ocorrencia.resumo)
        self.assertEqual(False, ocorrencia.estado)

    def test_criar_ocorrencia_funcionario_nao_esta_no_projeto(self):
        joao = Funcionario("Joao")
        with self.assertRaises(ValueError):
            self.projeto.criar_ocorrencia(
                joao,
                "qualquer descricao",
                TipoOcorrencia.TAREFA,
                PrioridadeOcorrencia.ALTA,
            )

    def test_criar_ocorrencia_sucesso(self):
        self.assertEqual(self.hugo.nome, self.ocorrencia.responsavel.nome)
        self.assertEqual(1, self.ocorrencia.chave)
        self.assertEqual("Qualquer resumo", self.ocorrencia.resumo)
        self.assertEqual(1, len(self.projeto.ocorrencias))

    def test_criar_ocorrencia_resumo_vazio(self):
        with self.assertRaises(ValueError):
            self.projeto.criar_ocorrencia(
                self.hugo, "", TipoOcorrencia.TAREFA, PrioridadeOcorrencia.ALTA
            )

    def test_criar_ocorrencia_resumo_poucas_letras(self):
        with self.assertRaises(ValueError):
            self.projeto.criar_ocorrencia(
                self.hugo, "nada", TipoOcorrencia.TAREFA, PrioridadeOcorrencia.ALTA
            )

    def test_criar_ocorrencia_gera_chave_correta(self):
        self.assertEqual(1, self.ocorrencia.chave)

        ocorrencia2 = self.projeto.criar_ocorrencia(
            self.hugo,
            "Qualquer outro resumo",
            TipoOcorrencia.TAREFA,
            PrioridadeOcorrencia.ALTA,
        )

        self.assertEqual(2, ocorrencia2.chave)

    def test_fechar_ocorrencia(self):
        self.ocorrencia.fechar()

        self.assertEqual(True, self.ocorrencia.estado)

    def test_mudar_funcionario(self):
        jorge = Funcionario("Jorge")
        self.projeto.adicionar_funcionario(jorge)
        self.projeto.mudar_funcionario(1, jorge)

    def test_mudar_funcionario_ocorrencia_fechada(self):
        self.ocorrencia.fechar()

        jorge = Funcionario("Jorge")
        self.projeto.adicionar_funcionario(jorge)

        with self.assertRaises(ValueError):
            self.projeto.mudar_funcionario(1, jorge)

    def test_mudar_funcionario_ocorrencia_invalida(self):
        jorge = Funcionario("Jorge")
        self.projeto.adicionar_funcionario(jorge)

        with self.assertRaises(ValueError):
            self.projeto.mudar_funcionario(0, jorge)

    def test_mudar_funcionario_nao_esta_no_projeto(self):
        jorge = Funcionario("Jorge")

        with self.assertRaises(ValueError):
            self.projeto.mudar_funcionario(1, jorge)

    def test_tipo_ocorrencia(self):
        ocorrencia = Ocorrencia(
            self.hugo,
            1,
            "Resumo da ocorrencia",
            TipoOcorrencia.TAREFA,
            PrioridadeOcorrencia.ALTA,
        )

        self.assertEqual(TipoOcorrencia.TAREFA, ocorrencia.tipo)

    def test_prioridade(self):
        ocorrencia = Ocorrencia(
            self.hugo,
            1,
            "Resumo da ocorrencia",
            TipoOcorrencia.TAREFA,
            PrioridadeOcorrencia.ALTA,
        )

        self.assertEqual(PrioridadeOcorrencia.ALTA, ocorrencia.prioridade)

    def test_mudar_prioridade_ocorrencia_aberta(self):
        self.ocorrencia.mudar_prioridade(PrioridadeOcorrencia.BAIXA)

        self.assertEqual(PrioridadeOcorrencia.BAIXA, self.ocorrencia.prioridade)

    def test_mudar_prioridade_ocorrencia_fechada(self):
        self.ocorrencia.fechar()

        with self.assertRaises(ValueError):
            self.ocorrencia.mudar_prioridade(PrioridadeOcorrencia.BAIXA)

    def test_mudar_prioridade_invalida(self):
        with self.assertRaises(ValueError):
            self.ocorrencia.mudar_prioridade(None)
