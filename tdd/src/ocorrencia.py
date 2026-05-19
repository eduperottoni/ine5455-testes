from funcionario import Funcionario
from enum import Enum


class TipoOcorrencia(Enum):
    TAREFA = 1
    BUG = 2
    REFATORACAO = 3


class PrioridadeOcorrencia(Enum):
    ALTA = 1
    MEDIA = 2
    BAIXA = 3


class Ocorrencia:
    def __init__(
        self,
        resp: Funcionario,
        chave: int,
        resumo: str,
        tipo: TipoOcorrencia,
        prioridade: PrioridadeOcorrencia,
    ):
        if not resp or not isinstance(resp, Funcionario):
            raise ValueError("responsável inválido")

        if len(resumo) < 10:
            raise ValueError("resumo inválido")

        self.responsavel = resp
        self.chave = chave
        self.resumo = resumo
        # False é aberta
        self.estado = False
        self.tipo = tipo
        self.prioridade = prioridade

    def fechar(self):
        self.estado = True

    def mudar_prioridade(self, nova_prioridade: PrioridadeOcorrencia):
        if not isinstance(nova_prioridade, PrioridadeOcorrencia):
            raise ValueError("prioridade inválida")

        if self.estado:
            raise ValueError("ocorrencia fechada")

        self.prioridade = nova_prioridade
