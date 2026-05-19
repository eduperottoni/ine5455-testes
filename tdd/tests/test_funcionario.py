import unittest
from funcionario import Funcionario


class TestFuncionario(unittest.TestCase):

    def test_criar_funcionario(self):
        funcionario = Funcionario("Eduardo")
        self.assertEqual("Eduardo", funcionario.nome)

    def test_criar_funcionario_sem_nome(self):
        with self.assertRaises(TypeError):
            _ = Funcionario()
