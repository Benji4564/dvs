class AbiAdt:

    def __init__(self):
        self._elemente = list()

    def leer(self):
        return len(self._elemente) == 0

    def __eq__(self, other):
        return self._elemente == other._elemente