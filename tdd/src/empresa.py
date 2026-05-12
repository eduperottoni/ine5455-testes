from funcionario import Funcionario
from projeto import Projeto


class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []
        self.projetos = []

    def adicionar_funcionario(self, funcionario: Funcionario):
        self.funcionarios.append(funcionario)

    def adicionar_projeto(self, projeto: Projeto):

        self.projetos.append(projeto)
