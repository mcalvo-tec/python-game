from Matrix import Matrix
from Mano import Mano

import random

# Clase que hereda de Matrix
# Clase hija que representa la matriz de tipo mano
# m[i][j] = objeto tipo Mano
class MatrixMano(Matrix):

    def __init__(self, _n, _m):
       """Constructor de clase MatrixMano"""
       self._n = _n
       self._m = _m
       self._elems = []
       
       # Inicializa la matriz de objetos Mano
       for i in range(self._n):
            self._elems.append([])
            for j in range(self._m):
                rand_value = random.randint(0, 10) # random inclusivo del 0-10
                mano = Mano(rand_value, self.setSymbol(rand_value))
                self._elems[i].append(mano)

       # Invoca al constructor de clase Matrix
       Matrix.__init__(self, _n, _m)

    def setSymbol(self, value):
        """Define el simbolo con respecto al enteri value"""
        if value >= 0 and value <= 3:
            return 'P' # Piedra
        elif value > 3 and value < 6:
            return 'L' # Papel
        else: return 'T' # Tijera
    
    def print_matrix(self):
        """Imprime en pantalla la matriz"""
        for i in range(self._n):
            for j in range(self._m):
                print("| {0} ".format(self.get_value_of_position(i, j).value), sep=',', end='')
            print('|\n')

    def get_value_of_position(self, i, j):
        """Obtiene el objeto en la posicion [i,j]"""
        return self._elems[i][j]
