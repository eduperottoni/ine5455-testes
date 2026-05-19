class Funcionario:
    def __init__(self, nome):
        self.nome = nome
        self.ocorrencias = []

    def adicionar_ocorrencia(self, ocorrencia):
        if len(self.ocorrencias) == 10:
            raise ValueError("Lista de ocorrencias já está lotada!")

        self.ocorrencias.append(ocorrencia)
