from Matrix import Matrix

# Clase que hereda de Matrix
# Clase hija que representa la matriz de tipo entero
class MatrixResult(Matrix):

    def __init__(self, _n, _m):
        """Inicializa la matriz con valor 0 en cada posición"""
        self._n = _n
        self._m = _m
        self._matriz = []
        
        # Llamar a funcion que crea la matrix n x m
        self.crear_matriz(self._n, self._m)
       
        # Invoca al constructor de clase Matrix
        Matrix.__init__(self, _n, _m)

    def crear_arreglo(self, N):
        """Función para crear un arreglo aleatorio, que será cada fila de la matriz"""
        arreglo = []
        for i in range(N):
            arreglo.append(0)
        return arreglo 

    def crear_matriz(self, fil, col):
        """Función para crear una matriz de fil FILAS y col COLUMNAS"""
        for i in range(fil):
            self._matriz.append(self.crear_arreglo(col)) 

    def define_elem(self, i, j, v):
        """Sobreescribe el valor de una celda"""
        self._matriz[i][j] = v

    def print_matrix(self):
        """Imprime los valores almacenados en la matriz"""
        for i in range(self._n):
            for j in range(self._m):
                # Imprime de una forma elegante la matriz
                print("| {0} ".format(self.get_value_of_position(i, j)), sep=',', end='')
            print('|\n')

    def get_value_of_position(self, i, j):
        """Obtiene el objeto en la posicion [i,j]"""
        return self._matriz[i][j]