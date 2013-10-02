class DifAuto(object):
    
    def __init__(self,valor,deriv):
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


    
    def __pow__(self,n):
        
        '''
        Operacion potencia para jets.
        '''
       
        return DifAuto (self.valor**n,n*self.valor**(n-1))
