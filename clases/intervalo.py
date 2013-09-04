class Intervalo(object):
    # Docstring
    """
    Esta clase provee aritmetica de intervalos.
    """
    def __init__(self, lo, hi=None):
        
        if hi is None:
            hi = lo
        if hi < lo:
            lo, hi = hi, lo
        self.lo = lo
        self.hi = hi
        
        
    def __repr__(self):
        #return "Intervalo(%s, %s)" % (self.min, self.max)
        return "Intervalo({}, {})".format(self.lo, self.hi)
    
    def __str__(self):
        return "[{}, {}]".format(self.lo, self.hi)
        
    # Para el IPython notebook:
    def _repr_html_(self):
        return "[{}, {}]".format(self.lo, self.hi)
    
#     def _repr_latex_(self):
#         return "$[{}^{}]$".format(self.min, self.max)

    def __add__(self, otro):
        return Intervalo(self.lo + otro.lo, self.hi + otro.hi)
    def __mul__(self,otro):
      return Intervalo(min(self.lo*otro.lo,self.lo*otro.hi,self.hi*otro.lo,self.hi*otro.hi),max(self.lo*otro.lo,self.lo*otro.hi,self.hi*otro.lo,self.hi*otro.hi))
    
        
    def __div__(self, otro):
      if otro.lo <= 0 <= otro.hi:
            raise ZeroDivisionError
      else:
                return Intervalo.__mul__(self,Intervalo(1./(otro.hi),1./(otro.lo)))
    
                 
      def test_division():
	a = Intervalo(1,2)
	b = Intervalo(1./4,1./2)
	c = a/b
	assert c.lo==2 and c.hi==8
	
      test_division()
      
      def test_division():
	a = Intervalo(2)
	b = Intervalo(1./4,1./2)
	c = a/b
	assert c.lo==4 and c.hi==8

      test_division()