from funcionario import Funcionario
from ocorrencia import Ocorrencia, TipoOcorrencia, PrioridadeOcorrencia


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

    def criar_ocorrencia(
        self,
        func: Funcionario,
        resumo: str,
        tipo: TipoOcorrencia,
        prioridade: PrioridadeOcorrencia,
    ) -> Ocorrencia:
        if func not in self.funcionarios:
            raise ValueError("Funcionário não está no projeto")

        ocorrencia = Ocorrencia(
            func, len(self.ocorrencias) + 1, resumo, tipo, prioridade
        )

        func.adicionar_ocorrencia(ocorrencia)
        self.ocorrencias.append(ocorrencia)
        return ocorrencia

    def mudar_funcionario(self, id_ocorrencia: int, func: Funcionario) -> None:
        if func not in self.funcionarios:
            raise ValueError("Funcionário não está no projeto")

        if not (0 < id_ocorrencia <= len(self.ocorrencias)):
            raise ValueError("id da ocorrência inválido")

        if self.ocorrencias[id_ocorrencia - 1].estado:
            raise ValueError("Ocorrência está fechada")

        ocorrencia = self.ocorrencias[id_ocorrencia - 1]
        ocorrencia.responsavel.ocorrencias.remove(ocorrencia)
        func.adicionar_ocorrencia(ocorrencia)
        ocorrencia.responsavel = func
