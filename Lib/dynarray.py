
from .adt import adt

class DynArray(adt):

    def __init__(self):
        super().__init__()

    def erhalteGegenstand(self, index):
        return self._elemente[index]

    def hinzufügen(self, neue):
        self._elemente.append( neue)

    def einfügen(self, index, neue):
        self._elemente.insert(index, neue)

    def setzeGegenstand(self, index, neue):
        self._elemente[index] = neue

    def löschen(self, index):
        self._elemente.pop(index)

    def erhalteLänge(self):
        return len(self._elemente)
