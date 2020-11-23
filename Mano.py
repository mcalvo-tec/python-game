# Clase que representa un posicion i,j en una matriz
# value: valor entero [0..10]
# symbol: char
#         P: Piedra, L: Papel, T: Tijera
class Mano:
    def __init__(self, value, symbol):
        self.value = value
        self.symbol = symbol