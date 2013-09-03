class Intervalo(object):
    # Docstring
    """
    Se define la clase 'Intervalo', y los m\'etodos para la aritm\'etica b\'asica de intervalos, 
    es decir, suma, resta, multiplicaci\'on y divisi\'on. Se incluyen otras funciones
    que ser\'an \'utiles.
    """
    def __init__(self,lo,hi=None):
        """ 
        Definimos las propiedades del objeto Intervalo a partir de sus bordes,
        lo y hi, donde lo <= hi. En el caso en que el intervalo s\'olo tenga
        un n\'umero, \'este se interpreta como un intervalo 'delgado' o 'degenerado'.
        """
        if hi is None:
            hi = lo
        
        self.lo = lo
        self.hi = hi
        
    def __repr__(self):
        return "Intervalo ({},{})".format(self.lo,self.hi)
    
    def __str__(self):
        # Esta funci\'on sirve con 'print'
        return "[{},{}]".format(self.lo,self.hi)

    def _repr_html_(self):
        return "[{}, {}]".format(self.lo, self.hi)
    
    def _repr_latex_(self):
        return "$[{}^{}]$".format(self.lo, self.hi)

    # Aqu\'i vienen las operaciones aritm\'eticas
    def __add__(self, otro):
        """
        Suma de intervalos
        """
        return Intervalo(self.lo + otro.lo, self.hi + otro.hi)

