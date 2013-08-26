class Intervalo(object):
    # Docstring
    """
    Esta clase provee aritmetica de intervalos.
    """
    def __init__(self, min, max=None):
        
        if max is None:
            max = min
        
        self.min = min
        self.max = max
        
        
    def __repr__(self):
        #return "Intervalo(%s, %s)" % (self.min, self.max)
        return "Intervalo({}, {})".format(self.min, self.max)
    
    def __str__(self):
        return "[{}, {}]".format(self.min, self.max)
        
    # Para el IPython notebook:
    def _repr_html_(self):
        return "[{}, {}]".format(self.min, self.max)
    
#     def _repr_latex_(self):
#         return "$[{}^{}]$".format(self.min, self.max)

    def __add__(self, otro):
        return Intervalo(self.min + otro.min, self.max + otro.max)

    def __sub__(self, otro):
        return Intervalo(self.min - otro.max, self.max - otro.min)

    def __mul__(self, otro):
        S = []
        S.append(self.min * otro.min)
        S.append(self.min * otro.max)
        S.append(self.max * otro.min)
        S.append(self.max * otro.max)

        return Intervalo(min(S), max(S))


    def __div__(self, otro):
        if otro.contains(0):
            raise ZeroDivisionError("Interval dividing by contains 0.")

        return self * otro.reciprocal()

    def reciprocal(self):
        return Intervalo(1.0 / self.max, 1.0 / self.min)

    def contains(self, x):
        return self.min <= x <= self.max
