class Intervalo(object):
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
    
    # def _repr_latex_(self):
    #     return "$[{}^{}]$".format(self.min, self.max)

    def __add__(self, otro):
        return Intervalo(self.min+otro.min, self.max+otro.max)

                
    # Esta es la funcion igualdad para intervalos
    def __eq__(self, otro):
        if self.min == otro.min and self.max == otro.max:
            return True
        else:
            return False