from funcionario import Funcionario


class Ocorrencia:
    def __init__(self, resp: Funcionario, chave: int, resumo: str):
        if not resp or not isinstance(resp, Funcionario):
            raise ValueError("responsável inválido")

        if len(resumo) < 10:
            raise ValueError("resumo inválido")

        self.responsavel = resp
        self.chave = chave
        self.resumo = resumo
        self.estado = False
