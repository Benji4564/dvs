from .abiadt import AbiAdt

class Stack(AbiAdt):

    def __init__(self):
        super().__init__()

    def top(self):
        return self._elemente[0]

    def push(self, neue):
        self._elemente.insert(0, neue)

    def pop(self):
        return self._elemente.pop(0)
