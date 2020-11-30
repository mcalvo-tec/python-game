# Clase base Matriz
class Matrix:
    _n = 0          # Filas
    _m = 0          # Columnas
    _matriz = None  # Arreglo Matriz
 
    def __init__(self, n, m):
        """Constructor clase base"""

    def setRows(self, rows):
        self._n = rows

    def setCols(self, cols):
        self._m = cols
 
    def get_cols(self):
        """ Devuelve el número de columnas en la matriz """
        return self._m
 
    def get_rows(self):
        """ Devuelve el número de filas en la matriz """
        return self._n
 
    cols = property(fget=get_cols)
    rows = property(fget=get_rows)

