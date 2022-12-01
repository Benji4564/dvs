
from .abiadt import AbiAdt

class DynArray(AbiAdt):

    def __init__(self):
        super().__init__()

    def getItem(self, index):
        return self._elemente[index]

    def append(self, neue):
        self._elemente.append( neue)

    def insertAt(self, index, neue):
        self._elemente.insert(index, neue)

    def setItem(self, index, neue):
        self._elemente[index] = neue

    def delete(self, index):
        self._elemente.pop(index)

    def getLength(self):
        return len(self._elemente)
