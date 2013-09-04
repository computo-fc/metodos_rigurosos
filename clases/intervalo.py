import numpy as np

class Intervalo(object):
    def __init__(self, lo, hi=None):
        
        if hi is None:
            hi = lo
        elif lo > hi:
            lo, hi = hi, lo
        
        self.lo = lo
        self.hi = hi
        
        
    def __repr__(self):
        #return "Intervalo(%s, %s)" % (self.lo, self.hi)
        return "Intervalo({}, {})".format(self.lo, self.hi)
    
    def __str__(self):
        return "[{}, {}]".format(self.lo, self.hi)
        
    # Para el IPython notebook:
    def _repr_html_(self):
        return "[{}, {}]".format(self.lo, self.hi)
    
    # def _repr_latex_(self):
    #     return "$[{}^{}]$".format(self.lo, self.hi)
    
    def __add__(self, otro):
        return Intervalo(self.lo+otro.lo, self.hi+otro.hi)
        
    def __and__(self, otro):
        if not isinstance(otro,Intervalo):
            otro = Intervalo(otro)
        if (self.lo > otro.hi) | (self.hi < otro.lo):
            return None
        else:
            a = np.hi([self.lo, otro.lo])
            b = np.lo([self.hi, otro.hi])
            return Intervalo(a,b)
    
    def __rand__(self, otro):
        return self & otro
    
