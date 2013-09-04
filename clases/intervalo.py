# -*- coding: utf-8 -*- 

class Intervalo(object):
    # Docstring
    """
    Se define la clase 'Intervalo', y los métodos para la aritmética básica de intervalos, 
    es decir, suma, resta, multiplicación y división. Se incluyen otras funciones
    que serán útiles.
    """
    def __init__(self,lo,hi=None):
        """ 
        Definimos las propiedades del objeto Intervalo a partir de sus bordes,
        lo y hi, donde lo <= hi. En el caso en que el intervalo sólo tenga
        un número, éste se interpreta como un intervalo 'delgado' o 'degenerado'.
        """
        if hi is None:
            hi = lo
        elif (hi < lo):
            lo, hi = hi, lo
        
        self.lo = lo
        self.hi = hi
        
    def __repr__(self):
        return "Intervalo ({},{})".format(self.lo,self.hi)
    
    def __str__(self):
        # Esta función sirve con 'print'
        return "[{},{}]".format(self.lo,self.hi)

    def _repr_html_(self):
        return "[{}, {}]".format(self.lo, self.hi)
    
    def _repr_latex_(self):
        return "$[{}^{}]$".format(self.lo, self.hi)

    # Aquí vienen las operaciones aritméticas
    def __add__(self, otro):
<<<<<<< HEAD
        return Intervalo(self.min+otro.min, self.max+otro.max)

                
    # Esta es la funcion igualdad para intervalos
    def __eq__(self, otro):
        if self.min == otro.min and self.max == otro.max:
            return True
        else:
            return False
=======
        """
        Suma de intervalos
        """
        try:
            return Intervalo(self.lo + otro.lo, self.hi + otro.hi)
        except:
            return self + Intervalo(otro)

    def __radd__(self, otro):
        return self + otro

>>>>>>> 58474ee792603457ec53917897b3070f8bc6b55b
