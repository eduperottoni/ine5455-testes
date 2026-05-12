from funcionario import Funcionario


class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario: Funcionario):
        self.funcionarios.append(funcionario)
