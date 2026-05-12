import unittest


class TestFuncionario(unittest.TestCase):

    def test_criar_funcionario(self):
        funcionario = Funcionario("Eduardo")
        self.assertEqual(funcionario.nome, "Eduardo")

    def test_criar_funcionario_sem_nome(self):
        with self.assertRaises(TypeError):
            _ = Funcionario()
