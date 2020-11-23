class Matrix:
    _n = 0
    _m = 0
    _matriz = None
 
    def __init__(self, n, m):
        """Constructor clase base"""
 
    def get_cols(self):
        """ Devuelve el número de columnas en la matriz """
        return self._m
 
    def get_rows(self):
        """ Devuelve el número de filas en la matriz """
        return self._n
 
    cols = property(fget=get_cols)
    rows = property(fget=get_rows)

