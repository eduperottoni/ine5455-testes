import unittest


class TestProjeto(unittest.TestCase):

    def test_criar_projeto(self):
        projeto = Projeto("Projeto Teste")
        self.assertEqual(projeto.nome, "Projeto Teste")

    def test_criar_projeto_sem_nome(self):
        with self.assertRaises(TypeError):
            _ = Projeto()
