from funcionario import Funcionario


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        if funcionario is None:
            raise ValueError("O funcionário não pode ser nulo.")
        self.funcionarios.append(funcionario)
