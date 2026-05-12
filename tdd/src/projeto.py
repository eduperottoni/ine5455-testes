from funcionario import Funcionario


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario: Funcionario):
        if funcionario is None:
            raise ValueError("O funcionário não pode ser nulo.")

        if any(funcionario.nome == f.nome for f in self.funcionarios):
            raise ValueError("O funcionário já está no projeto.")

        self.funcionarios.append(funcionario)
