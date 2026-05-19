from funcionario import Funcionario
from ocorrencia import Ocorrencia


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []
        self.ocorrencias = []

    def adicionar_funcionario(self, funcionario: Funcionario):
        if funcionario is None:
            raise ValueError("O funcionário não pode ser nulo.")

        if any(funcionario.nome == f.nome for f in self.funcionarios):
            raise ValueError("O funcionário já está no projeto.")

        self.funcionarios.append(funcionario)

    def criar_ocorrencia(self, func: Funcionario) -> Ocorrencia:
        if func not in self.funcionarios:
            raise ValueError("Funcionário não está no projeto")

        ocorrencia = Ocorrencia(func, 3, "")

        self.ocorrencias.append(ocorrencia)
        return ocorrencia
