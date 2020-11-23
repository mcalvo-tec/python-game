from MatrixMano import MatrixMano
from MatrixResult import MatrixResult

import csv

class Partida:
    _rows = 0
    _cols = 0
    _empatates = 0
    _victoriasMatriz1 = 0
    _victoriasMatriz2 = 0
    _matriz1 = None
    _matriz2 = None
    _matrizResultado = None
    _file = None

    def __init__(self, _rows, _cols):
        self._rows = _rows
        self._cols = _cols
        self.init_values()
        
    def init_values(self):
        """Inicializar las matrices correspondientes"""
        self._matriz1 = MatrixMano(self._rows, self._cols)
        self._matriz2 = MatrixMano(self._rows, self._cols)
        self._matrizResultado = MatrixResult(self._rows, self._cols)

    def print_matriz_1(self):
        """Funcion que imprime la matriz_1 tipo objeto mano"""
        print("*****   Matriz 1   *****")
        print("")
        self._matriz1.print_matrix()
        print("***** Fin Matriz 1 *****")
        print("")

    def print_matriz_2(self):
        """Funcion que imprime la matriz_2 tipo objeto mano"""
        print("*****   Matriz 2   *****")
        print("")
        self._matriz2.print_matrix()
        print("***** Fin Matriz 2 *****")
        print("")

    def print_matriz_resultado(self):
        """Funcion que imprime la matriz_1 tipo objeto mano"""
        print("*****   Matriz Resultado   *****")
        print("***** 0: Empate            *****")
        print("***** 1: Matriz_1          *****")
        print("***** 2: Matriz_2          *****")
        print("")
        self._matrizResultado.print_matrix()
        print("***** Fin Matriz Resultado *****")
        print("")

    def save_game(self):
        self._file = open('matriz-resultado.csv', 'w')
        with self._file:
            writer = csv.writer(self._file)
            writer.writerow(["**** Matriz Resultado ****"])
            writer.writerows(self._matrizResultado._matriz)
            
        print("Partida Guardada")

    


    

    