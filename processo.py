class Processo:
    def __init__(self, nome: str, id: int, valor):
        self.nome = str
        self.id = int
        self.valor = []

    @property
    def nome(self) -> str:
        return self.nome

    @nome.setter
    def nome(self, nome: str):
        self.nome = nome

    @property
    def id(self) -> int:
        return self.id

    @id.setter
    def id(self, value: int):
        self.id = value

    @property
    def valor(self) -> list:
        return self.valor

    @valor.setter
    def valor(self, valor_add: int):
        if len(self.valor) <= 10:
            self.valor.append(valor_add)
        else:
            raise ValueError("Array cheio")
