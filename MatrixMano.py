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
       self._matriz = []
       
       # Inicializa la matriz de objetos Mano
       for i in range(self._n):
            self._matriz.append([])
            for j in range(self._m):
                rand_value = random.randint(0, 10) # random inclusivo del 0-10
                mano = Mano(rand_value, self.set_symbol(rand_value))
                self._matriz[i].append(mano)

       # Invoca al constructor de clase Matrix
       Matrix.__init__(self, _n, _m)

    def set_symbol(self, value):
        """Define el simbolo con respecto al enteri value"""
        if value >= 0 and value <= 3:
            return 'P' # Piedra
        elif value > 3 and value < 6:
            return 'L' # Papel
        else: return 'T' # Tijera
    
    def print_matrix(self):
        """Imprime en pantalla la matriz"""
        value = 0
        strValue = ""
        for i in range(self._n):
            for j in range(self._m):
                value = self.get_value_of_position(i, j).getValor()
                strValue = " " + str(value) if value != 10 else str(value)
                print("\t {0} ".format(strValue + "-" + self.get_value_of_position(i, j).getSimbolo()), sep=',', end='')
            print('\n')

    def get_value_of_position(self, i, j):
        """Obtiene el objeto en la posicion [i,j]"""
        return self._matriz[i][j]
