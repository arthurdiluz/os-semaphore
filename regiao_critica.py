class RegiaoCritica:
    def __init__(self):
        self.vetor = []

    @property
    def vetor(self) -> list:
        return self.vetor

    @vetor.setter
    def vetor(self, valor: list):
        self.vetor_add(valor)

    def vetor_add(self, lista: list):
        if len(lista) + len(self.vetor) <= 1000:
            for valor in lista:
                self.vetor.append(valor)
        else:
            raise OverflowError(F"Vetor cheio! {len(self.vetor)} elementos.")

    def vetor_rem(self):
        if self.vetor:
            self.vetor.pop(0)
        else:
            raise IndexError("Vetor vazio.")
