from funcionario import Funcionario
from projeto import Projeto


class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []
        self.projetos = []

    def adicionar_funcionario(self, funcionario: Funcionario):
        if funcionario is None:
            raise ValueError("O Funcionário não pode ser nulo.")

        if any(funcionario.nome == f.nome for f in self.funcionarios):
            raise ValueError("O funcionário já está na empresa.")

        self.funcionarios.append(funcionario)

    def adicionar_projeto(self, projeto: Projeto):
        if projeto is None:
            raise ValueError("O projeto não pode ser nulo.")

        if any(projeto.nome == p.nome for p in self.projetos):
            raise ValueError("O projeto já está na empresa.")

        self.projetos.append(projeto)
