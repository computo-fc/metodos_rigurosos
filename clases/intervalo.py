
# -*- coding: utf-8 -*- 
from sympy import mpmath as mp
class Intervalo(object):
    """
    Se define la clase 'Intervalo', y los métodos para la aritmética básica de intervalos,
    es decir, suma, resta, multiplicación y división. Se incluyen otras funciones
    que serán útiles.
    """
    def __init__(self, lo, hi=None):
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
        return "Intervalo [{},{}]".format(self.lo,self.hi)
    
    def __str__(self):
        # Esta función sirve con 'print'
        return "[{},{}]".format(self.lo,self.hi)

    def _repr_html_(self):
        return "[{}, {}]".format(self.lo, self.hi)
    
    def _repr_latex_(self):
        return "$[{}, {}]$".format(self.lo, self.hi)

    # Aquí vienen las operaciones aritméticas
    def __add__(self, otro):
        """
        Suma de intervalos
        """
        try:
            return Intervalo(self.lo + otro.lo, self.hi + otro.hi)
        except:
            return self + Intervalo(otro)

    def __radd__(self, otro):
        return self + otro
        
        
        
    def __mul__(self, otro):
      
        return self._mul2(otro)
      
      
      
    def _mul1(self, otro):
        try:
            S=[self.lo*otro.lo , self.lo * otro.hi , self.hi * otro.lo , self.hi * otro.hi ]
            return Intervalo( min(S), max(S) )
        except:
            return self * Intervalo(otro)

            
    def _mul2(self, otro):
        """Multiplicacion de intervalos, evaluando todos los casos posibles """
        try:
            if self.lo >= 0 :
                if otro.lo >= 0:
                    return Intervalo(self.lo * otro.lo , self.hi * otro.hi)
                elif otro.hi <= 0 :
                    return Intervalo(self.hi * otro.lo , self.lo * otro.hi)
                elif otro.lo <= 0 and otro.hi >= 0:
                    return Intervalo(self.hi * otro.lo , self.hi * otro.hi)
                
            elif self.hi <= 0:
                if otro.hi <= 0:
                    return Intervalo(self.hi * otro.hi , self.lo * otro.lo)
                elif otro.lo >= 0:
                    return Intervalo(self.lo * otro.hi , self.hi * otro.lo)
                elif otro.lo <= 0 and otro.hi >= 0:
                    return Intervalo(self.lo * otro.hi , self.lo * otro.lo) 
                     
            elif self.lo <= 0 and self.hi >= 0:
                if otro.lo >= 0:
                    return Intervalo(self.lo * otro.hi , self.hi * otro.hi)
                elif otro.hi <= 0:
                    return Intervalo(self.hi * otro.lo , self.lo * otro.lo)         
                elif otro.lo <= 0 and otro.hi >= 0:   
                    return Intervalo(min(self.hi * otro.lo , self.lo * otro.hi) , max(self.hi * otro.hi , self.lo * otro.lo))
                    
                
        except:
            return self * Intervalo(otro)

     
    def __rmul__(self, otro):
        return self * otro

    # Esta es la funcion igualdad para intervalos
    def __eq__(self, otro):
        """
        función igualdad para intervalos 

        """
        try:
            if self.lo == otro.lo and self.hi == otro.hi:
                return True
            else:
                return False
        except:
            if self.lo == Intervalo(otro).lo and self.hi == Intervalo(otro).hi:
                return True
            else:
                return False
  

    #interseccion
    def __and__(self, otro):
        """
        Intersección de intervalos
        Funciona con la sintaxis & (como el AND bitwise)
        """
        if not isinstance(otro,Intervalo):
            otro = Intervalo(otro)

        if (self.lo > otro.hi) | (self.hi < otro.lo):
            return None

        else:
            a = max( self.lo, otro.lo )
            b = min( self.hi, otro.hi )
            return Intervalo(a,b)
    
    #interseccion por la izquierda
    def __rand__(self, otro):
        """
        Interseccion de intervalos (por la izquierda)
        """
        return self & otro
    
    #negativo del intervalo
    def __neg__(self):
        """
        Devuelve el valor negativo del intervalo
        """
        return Intervalo(-self.hi, -self.lo)

    #Funcion reciproco
    def reciprocal(self):
        """
        Devuelve un intervalo con los valores recíprocos
        """
        if self.lo <= 0 <= self.hi:
            #si el intervalo contiene el cero debe de aparecer un error
            raise ZeroDivisionError
        else:
            return Intervalo(1.0/self.hi,1.0/self.lo)

    #division con denominadores que no contienen al cero    
    def __div__(self, otro):
	"""
	División
	"""
        if not isinstance(otro, Intervalo):
            otro = Intervalo(otro)

        if otro.lo <= 0 <= otro.hi:
            raise ZeroDivisionError

        else:
            return self * otro.reciprocal()
    
    #división reversa
    def __rdiv__(self, otro):
	"""
	División revrsa para poder usar floats en el numerador
	"""
        if not isinstance(otro, Intervalo):
            otro = Intervalo(otro)

        return Intervalo.__div__(otro, self)

    def middle(self):
        """
        Calcula el punto medio del intervalo
        """
        return (self.lo+self.hi)/2
        
    def radio(self):
        """
        Calcula el radio del intervalo
        """
        return (self.hi-self.lo)/2
        
    def width(self):
        """
        Cacula la anchura
        """

        return self.hi-self.lo
        
    def abs(self):
        
        return max([abs(self.lo),abs(self.hi)])
	

    #funciones elementales para intervalos
      
    def exp(self):
	"""
	Calcula la exponencial de un intervalo.
	"""
	
        return Intervalo(mp.exp(self.lo), mp.exp(self.hi))



    def log(self):
	"""
	Calcula el logaritmo de un intervalo.
	"""
	
	Dom_log = Intervalo(0,mp.inf)
		
	if self.lo >= 0 :
	  return Intervalo(mp.log(self.lo), mp.log(self.hi))
	

	elif self.hi < 0:
	  raise ValueError("La función logaritmo no puede tomar intervalos totalmente negativos. El intervalo [%f,%f] es negativo." % (self.lo, self.hi) )
	

	elif self.lo < 0 and self.hi >= 0:
	  Dom_restr = Dom_log & Intervalo(self.lo,self.hi)
	  print "WARNING: El intervalo contiene numeros negativos. Se toma el intervalo restringido [%f,%f]."\
		% (Dom_restr.lo, Dom_restr.hi)
	  return Intervalo(mp.log(Dom_restr.lo), mp.log(Dom_restr.hi))
