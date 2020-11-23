from Matrix import Matrix

# Clase que hereda de Matrix
# Clase hija que representa la matriz de tipo entero
class MatrixResult(Matrix):

    def __init__(self, _n, _m):
        """Inicializa la matriz con valor 0 en cada posición"""
        self._n = _n
        self._m = _m
        self._elems = []
        for i in range(self._n):
            self._elems.append([])
            for j in range(self._m):
                self._elems[i].append(0)
       
        # Invoca al constructor de clase Matrix
        Matrix.__init__(self, _n, _m)

    def define_elem(self, i, j, v):
        """ Sobreescribe el valor de una celda """
        self._elems[i][j] = v

    def print_matrix(self):
        """ Imprime los valores almacenados en la matriz """
        for i in range(self._n):
            for j in range(self._m):
                # Imprime de una forma elegante la matriz
                print("| {0} ".format(self.get_value_of_position(i, j)), sep=',', end='')
            print('|\n')

    def get_value_of_position(self, i, j):
        return self._elems[i][j]