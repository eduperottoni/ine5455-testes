class Funcionario:
    def __init__(self, nome):
        self.nome = nome
        self.ocorrencias = []

    def adicionar_ocorrencia(self, ocorrencia):
        if self.ocorrencias_abertas() >= 10:
            raise ValueError("Lista de ocorrencias já está lotada!")

        self.ocorrencias.append(ocorrencia)

    def ocorrencias_abertas(self):
        return sum(1 for o in self.ocorrencias if not o.estado)
