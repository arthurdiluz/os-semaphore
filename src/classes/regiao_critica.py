class CriticalSection:
    def __init__(self):
        self.vector = []

    def vetor_add(self, value: int):
        if len(self.vector) < 1000:
            self.vector.append(value)
        else:
            raise IndexError("Critical section is full")

    def vetor_rem(self):
        if self.vector:
            self.vector.pop(0)
        else:
            raise IndexError("Critical section is empty")
