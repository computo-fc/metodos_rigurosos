import numpy as np

class Intervalo(object):
    def __init__(self, min, max=None):
        
        if max is None:
            max = min
        elif min > max:
            min, max = max, min
        
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
    
    # def _repr_latex_(self):
    #     return "$[{}^{}]$".format(self.min, self.max)
    
    def __add__(self, otro):
        return Intervalo(self.min+otro.min, self.max+otro.max)
        
    def __and__(self, otro):
        if not isinstance(otro,Intervalo):
            otro = Intervalo(otro)
        if (self.min > otro.max) | (self.max < otro.min):
            return None
        else:
            a = np.max([self.min, otro.min])
            b = np.min([self.max, otro.max])
            return Intervalo(a,b)
    
    def __rand__(self, otro):
        return self & otro
    
