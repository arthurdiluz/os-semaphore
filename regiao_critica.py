class RegiaoCritica:
    def __init__(self):
        self.vetor = []

    def vetor_add(self, valor: int):
        if len(self.vetor) < 1000:
            self.vetor.append(valor)
        else:
            raise IndexError("região critica cheia")

    def vetor_rem(self):
        if self.vetor:
            self.vetor.pop(0)
        else:
            raise IndexError("região critica vazia")
