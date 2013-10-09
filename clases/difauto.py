import numpy
math = numpy
#math = mpmath


class DifAuto(object):
    
    def __init__(self, valor, deriv):
        self.valor=valor
        self.deriv=deriv
        
        
    #Representaciones
    
    def __repr__(self):
        return "DifAuto [{},{}]".format(self.valor,self.deriv)
    
    def __str__(self):
        return "[{},{}]".format(self.valor,self.deriv)

    def _repr_html_(self):
        reprn = "[{}, {}]".format(self.valor, self.deriv)
        reprn = reprn.replace("inf", r"&infin;")
        return reprn
    
    def _repr_latex_(self):
        return "$[{}, {}]$".format(self.valor, self.deriv)


    def __add__(self, otro):
        
        try:
            return DifAuto(self.valor + otro.valor, self.deriv + otro.deriv)
        except:
            return self + DifAuto(otro, 0)
            
    def __radd__(self, otro):
        
        return self + otro

    def __sub__(self, otro):
        
        try:
            return DifAuto(self.valor - otro.valor, self.deriv - otro.deriv)
        except:
            return self - DifAuto(otro,0)

    def __rsub__(self, otro):
        
        return self - otro
        
    def __pow__(self, n):
        
        '''
        Operacion potencia para jets.
        '''
       
        return DifAuto(self.valor**n, n*self.valor**(n-1)*self.deriv)
        
    def __mul__(self, otro):
        
        try:        
            return DifAuto(self.valor*otro.valor, self.valor*otro.deriv + self.deriv*otro.valor)
        except:
            return self*DifAuto(otro, 0)

    def __rmul__(self, otro):
        
        return self*otro

    def __div__(self, otro):
        
        try:
            return DifAuto(self.valor/otro.valor, (self.deriv*otro.valor - self.valor*otro.deriv)/otro.valor**2)
        except:
            return self/DifAuto(otro,0)

    def __rdiv__(self, otro):
        
        return self/otro

    def exp(self):
        
        return DifAuto(math.exp(self.valor), math.exp(self.valor)*self.deriv)
        
    def log(self):

            return DifAuto(math.log(self.valor), self.deriv/self.valor)
            
    def sin(self):
        
        return DifAuto(math.sin(self.valor), math.cos(self.valor)*self.deriv)
        
    def cos(self):
        
        return DifAuto(math.cos(self.valor), -math.sin(self.valor)*self.deriv)
            

