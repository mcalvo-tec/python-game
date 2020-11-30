# Clase que representa un posicion i,j en una matriz
# value: valor entero [0..10]
# symbol: char
#         P: Piedra, L: Papel, T: Tijera
class Mano:
    _value = 0
    _symbol = ""
    # Constructor de la clase
    def __init__(self, value, symbol):
        self._value = value
        self._symbol = symbol

    def setValor(self, valor):
        self._value = valor

    def setSimbolo(self, simbolo):
        self._symbol = simbolo

    def getValor(self):
        return self._value

    def getSimbolo(self):
        return self._symbol
