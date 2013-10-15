## Libreria de tests para la clase DifAuto


from difauto import *

import numpy as np

math=np

#math=mp

def TwoReals(u=-100.0,v=100.0):
    """
    Lanza dos reales de -100 a 100 con medida uniforme
    """
    num=np.random.uniform(u,v)
    num2=np.random.uniform(u,v)
        
    return num,num2

def Real(u=-100.0,v=100.0):
    """
    Lanza un numero aleatorio entre -10 a 10 con medida uniforme
    """
    return math.random.uniform(u,v)
    
def test_suma():
    
    '''
    Test de la suma de la clase jet
    '''
    
    for k in range(0,100):
    
        num,num2=TwoReals()
        numb,numb2=TwoReals()
    
        a=DifAuto(num,num2)
        b=DifAuto(numb,numb2)
    
        c=a+b
    
        assert c.valor==a.valor+b.valor  and c.deriv==a.deriv+b.deriv
    
    
def test_resta():
    
    '''
    Test de la resta de la clase jet
    '''
    
    for k in range(0,100):
    
        num,num2=TwoReals()
        numb,numb2=TwoReals()
    
        a=DifAuto(num,num2)
        b=DifAuto(numb,numb2)
    
        c=a-b
    
        assert c.valor==a.valor-b.valor  and c.deriv==a.deriv-b.deriv
        
    
def test_multiplicacion():
    
    '''
    Test de multiplicacion de la clase jet
    '''
    for k in range(0,100):
        
        num,num2=TwoReals()
        numb,numb2=TwoReals()
        
        a=DifAuto(num,num2)
        b=DifAuto(numb,numb2)
        
        c=a*b
        
        assert c.valor== a.valor*b.valor and c.deriv== a.valor*b.deriv+a.deriv*b.valor
    
    
def test_division():
    
    '''
    Test de division de la clase intervalo
    '''
    
    for k in range(0,100):
        
        num,num2=TwoReals()
        numb,numb2=TwoReals()
        
        #Se omite precisar que numb sea diferente de cero dado que la probabilidad de obtenerlo es nula
        
        a=DifAuto(num,num2)
        b=DifAuto(numb,numb2)
        
        c=a/b
        
        assert c.valor==a.valor/b.valor and c.deriv==(a.deriv*b.valor-a.valor*b.deriv)/(b.valor**2)
    
    
def test_potencia():

    '''
    Test de la operacion potencia para jets
    '''    
    
    for k in range(0,100):
        
        num,num2=TwoReals(0.0,10.0)
        
        num3=Real(-10.0,10.0)
        
        a=DifAuto(num,num2)**num3
        
        assert a.valor==num**num3 and a.deriv== num3*num**(num3-1)*num2
        
        
def test_log():
    '''
    Test de logaritmo para la clase jet
    '''
    
    for k in range(0,100):
    
        num,num2=Real(1.0,100.0), Real(-100.0,100.0)
    
        a=math.log(DifAuto(num,num2))
    
        assert a.valor==math.log(num) and a.deriv==num2/num
        
def test_exp():
    '''
    Test de funcion exponencial para la clase jet
    '''    
    
    for k in range(0,100):
    
        num,num2=Real(1.0,100.0),Real(-100.0,100.0)
    
        a=math.exp(DifAuto(num,num2))
    
        assert a.valor==math.exp(num) and a.deriv==num2*math.exp(num)

    
def test_sin():
    '''
    test del coseno para jets: 101 eventos con jets aleatorios
    '''
    for k in range(0,100):
        
        num=Real()
        a=math.sin(DifAuto(num,1))
    
    
        assert a.valor==math.sin(num) and a.deriv==math.cos(num)
    
def test_cos():
    '''
    test del coseno para jets: 101 eventos con jets aleatorios
    '''
    for k in range(0,100):
        
        num=Real()
        a=math.cos(DifAuto(num,1))
    
    
        assert a.valor==math.cos(num) and a.deriv==-math.sin(num)
        
        
def All_tests():    
    '''
    Se corren todos los test de la clase jet
    '''
    test_suma()
    test_resta()
    test_multiplicacion()
    test_division()
    test_potencia()
    test_log()
    test_exp()
    test_sin()
    test_cos()    
    
    
    
    
    
    
    
    
    
    
    