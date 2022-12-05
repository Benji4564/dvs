from abiadt import AbiAdt

class Stapel(AbiAdt):

    def __init__(self):
        super().__init__()

    def oberste(self):
        return self._elemente[0]

    def rauflegen(self, neue):
        self._elemente.insert(0, neue)

    def runternehmen(self):
        return self._elemente.pop(0)
