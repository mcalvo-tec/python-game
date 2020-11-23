from MatrixMano import MatrixMano
from MatrixResult import MatrixResult

import csv

# Clase Partida, encargada de representar el juego
class Partida:
    _rows = 0               # Cantidad de filas
    _cols = 0               # Cantidad de filas
    _empates = 0            # Contador empates
    _victoriasMatriz1 = 0   # Contador victorias de matriz1
    _victoriasMatriz2 = 0   # Contador victorias de matriz1
    _matriz1 = None         # Matriz1 de objetos tipo Mano
    _matriz2 = None         # Matriz1 de objetos tipo Mano
    _matrizResultado = None # Matriz de enteros, guarda el resultado 
    _file = None            # Archivo que guarda la partida con la matriz resultado

    def __init__(self, _rows, _cols):
        self._rows = _rows
        self._cols = _cols
        self._matriz1 = []
        self._matriz2 = []
        self._matrizResultado = []
        # Llamada a funcion auxiliar de inicio
        self.init_values()
        
    def init_values(self):
        """Inicializar las matrices correspondientes"""
        self._matriz1 = MatrixMano(self._rows, self._cols)
        self._matriz2 = MatrixMano(self._rows, self._cols)
        self._matrizResultado = MatrixResult(self._rows, self._cols)

    def print_matriz_1(self):
        """Funcion que imprime la matriz_1 tipo objeto mano"""
        print("*****   Matriz 1   *****\n")
        self._matriz1.print_matrix()
        print("***** Fin Matriz 1 *****\n")

    def print_matriz_2(self):
        """Funcion que imprime la matriz_2 tipo objeto mano"""
        print("*****   Matriz 2   *****\n")
        self._matriz2.print_matrix()
        print("***** Fin Matriz 2 *****\n")
    

    def print_matriz_resultado(self):
        """Funcion que imprime la matriz_1 tipo objeto mano"""
        print("*****   Matriz Resultado   *****")
        print("***** 0: Empate            *****")
        print("***** 1: Matriz_1          *****")
        print("***** 2: Matriz_2          *****")
        print("")
        self._matrizResultado.print_matrix()
        print("***** Fin Matriz Resultado *****\n")

    def save_game(self):
        """Funcion que escribe en archivo la matriz resultado"""
        print("\n** Guardando partida ...\n")
        with open('savep.csv', 'w') as self._file:
            writer = csv.writer(self._file)     
            writer.writerow(str(self._rows))                # Numero de filas
            writer.writerow(str(self._cols))                # Numero de columnas
            writer.writerows(self._matrizResultado._matriz) # Matriz de resultado
   
        print("** Partida Guardada!\n")

    def load_game(self):
        """Lee de archivo la matriz resultado"""
        try:
            print("\n** Leyendo archivo savep.py ...\n")
            with open("savep.csv", 'r', encoding = 'utf-8') as self._file:
                csv_reader = csv.reader(self._file)
                line_count = 1
                rows = 0
                cols = 0
                i = 0
                result = [] # Matriz que se conforma de la lectura del archivo
                for row in csv_reader:
                    if line_count == 1:
                        rows = int(f'{"".join(row)}')
                        line_count += 1

                    elif line_count == 2:
                        cols = int(f'{"".join(row)}')
                        line_count += 1
                        # Matriz Resultado: rows x cols
                        saveGameMatriz = MatrixResult(rows, cols)

                    else:
                        # string de fila separada por comas
                        str_row = f'{",".join(row)}'
                        str_row = str_row.split(',')

                        result.append([])
                        j = 0
                        for element in str_row:
                            result[i].append(element)
                            j += 1

                        line_count += 1
                        i += 1
                print(f'** Lectura finalizada, lineas leidas de archivo: {line_count-1}\n')
                print("** Cargando ultima partida ...\n")
                saveGameMatriz._matriz = result
                saveGameMatriz.print_matrix()
                print("** Partida cargada!\n")

        except:
            print("\nERROR: Archivo no encontrado\n")

    # Retorna 1: Gana symbol1 de MatrizMano_1[i][j]
    #         2: Gana symbol2 de MatrizMano_2[i][j]
    #         0: Empate, symbol1 = symbol2
    # Posibles valores symbol1 y symbol2:
    #         P: Piedra, L: Papel, T: Tijera
    def set_winner(self, symbol1, symbol2):
        """Determina si hay ganador comparando symbol1 con symbol2"""
        # Empate
        if(symbol1 == symbol2):
            return 0
        # Determinar ganador segun reglas
        # Regla 1: T < P < L, P = symbol1    
        if(symbol1 == 'P'):
            if(symbol2 == 'T'):
                return 1
            else: # symbol2 = L 
                return 2 
        # Regla 2: P < L < T, L = symbol1 
        elif (symbol1 == 'L'):
            if(symbol2 == 'P'):
                return 1
            else: # symbol2 = T
                return 2
        # Regla 3: L < T < P, T = symbol1  
        else:
            # symbol1 = T
            if(symbol2 == 'L'):
                return 1
            else: # symbol2 = P
                return 2

    # Compara posicion [i][j] de _matriz1 y _matriz2
    # Con base en las reglas determina al ganador o empate.
    # Actualiza los contadores de victorias y empate por partida
    # Va definiendo la matriz resultado
    # Determina al ganador
    def play(self):
        """Inicia la ejecucion de una partida"""
        posResult = -1
        symbol1 = ""
        symbol2 = ""
        self.print_matriz_1()
        self.print_matriz_2()
        print("\n*** Iniciando partida ...\n")
        print("\n*** Determinando ganador ...\n")
        for i in range(self._rows):
            for j in range(self._cols):
                symbol1 = self._matriz1.get_value_of_position(i, j).symbol
                symbol2 = self._matriz2.get_value_of_position(i, j).symbol
                posResult = self.set_winner(symbol1, symbol2)
                # Actualizar contadores segun resultado de ganador
                self.updateCounters(posResult)
                self._matrizResultado.define_elem(i,j, posResult)

        print(" --- Resultados Finales --- ")
        print(f'  *) Victorias Matriz 1: {self._victoriasMatriz1}')
        print(f'  *) Victorias Matriz 2: {self._victoriasMatriz2}')
        print(f'  *) Empates: {self._empates}')
        print(" \n ------- GANADOR ------- \n")
        
        if(self._victoriasMatriz1 == self._victoriasMatriz2):
            print(" *** PARTIDA EMPATADA ***\n")
        elif(self._victoriasMatriz1 > self._victoriasMatriz2):
            print(" *** MATRIZ_1 ***\n")
        else:
            print(" *** MATRIZ_2 ***\n")
        
        print(" ----- FIN GANADOR ----- \n")
        print("\n*** FIN de la partida ***\n")


    def updateCounters(self, counter):
        if(counter == 1):
            self._victoriasMatriz1 += 1
        elif (counter == 2):
            self._victoriasMatriz2 += 1
        else:
            self._empates += 1
    
        

    


    

    