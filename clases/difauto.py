# -*- coding: utf-8 -*- 

import numpy
math =  numpy

class DifAuto(object):
    
    def __init__(self, valor, deriv=None):
        if deriv is None:
            deriv = 0
        self.valor = valor
        self.deriv = deriv
        
        
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


    def __pow__(self,n):
        '''
        Operacion potencia para jets.
        '''
        return DifAuto (self.valor**n, n*self.valor**(n-1)*self.deriv)

    def __add__(self, otro):
        """
        Derivación Suma
        """
        try:
            return DifAuto (self.valor + otro.valor, self.deriv + otro.deriv)
        
        except:
            return self + DifAuto(otro)
            
    def __radd__(self, otro):
        
        return self + otro
        
    def __mul__(self, otro):
        """
        Derivación Multiplicación
        """
        try:
            return DifAuto ( self.valor * otro.valor, self.valor * otro.deriv + self.deriv * otro.valor)
        
        except:
            return self * DifAuto (otro)
        
    def __rmul__(self, otro):
        return self * otro
    
    def __sub__(self, otro):
        """
        Resta de Intervalos
        """
        if not isinstance(otro, DifAuto):
            otro = DifAuto (otro)
        
        return DifAuto (self.valor - otro.valor, self.deriv - otro.deriv)                
        
    def __rsub__(self, otro):
        
        if not isinstance(otro, DifAuto):
            otro = DifAuto (otro)
            
        return DifAuto.__sub__(otro, self)
        
    def __div__(self, otro):
        """
        División
        """
        if not isinstance(otro, DifAuto):
            otro = DifAuto (otro)
        
        a = DifAuto.__pow__(otro,-1)        
        
        return DifAuto.__mul__(self, a)

    def __rdiv__(self, otro):
        """
        División revrsa para poder usar floats en el numerador
        """
        if not isinstance(otro, DifAuto):
            otro = DifAuto(otro)

        return DifAuto.__div__(otro, self)

    def exp(self):
        """
        Exponencial
        """
        return DifAuto (math.exp(self.valor), math.exp(self.valor) * self.deriv)
       
    def log(self):
        """
        Logaritmo
        """
        return DifAuto (math.log(self.valor), 1./(self.valor) * self.deriv)
    
    def sin(self):
        """
        Seno
        """
        return DifAuto (math.sin(self.valor), math.cos(self.valor) * self.deriv)
            
    def cos(self):
        """
        Coseno
        """
        return DifAuto (math.cos(self.valor), -math.sin(self.valor) * self.deriv)

    def tan(self):
        """
        Tangente
        """
        return self.sin()/self.cos()
            
        
def exp(x):
    try:
        return x.exp()
    except:
        return math.exp(x)    
    
def log(x):
    try:
        return x.log()
    except:
        return math.log(x)

def cos(x):
    try:
        return x.cos()
    except:
        return math.cos(x)

def sin(x):
    try:
        return x.sin()
    except:
        return math.sin(x)

def tan(x):
    try:
        return x.tan()
    except:
        return math.tan(x)

