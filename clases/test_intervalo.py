# Escribimos funciones con el nombre test_ALGO

from intervalo import *

import numpy as np

def test_adicion():
    a = Intervalo(1, 2)
    b = Intervalo(2, 3)
    c = a + b

    # Quiero checar que c, definido asi, esta bien:
    assert c.lo == 3 and c.hi == 5

def test_multiplicacion():
    # Test de la multiplicacion (Laura y Leon)
    a = Intervalo(1, 2)
    b = Intervalo(3, 4)
    c = Intervalo(6,-6)
    d = Intervalo(0,10)
    e = Intervalo(-0.5,0.2)
    f = 7
    g = 0.5
    h = Intervalo(-30,-20)
    ab = a*b
    ac = a*c
    ad = a*d
    ae = a*e
    af = a*f
    ag = a*g
    ah = a*h
    cc = c*c
    gc = g*c
    # Quiero checar que todas la multiplicaciones de arriba, definidas asi, estan bien:
    assert ab.lo == 3 and ab.hi == 8 
    assert ac.lo == -12 and ac.hi == 12 
    assert ad.lo == 0 and ad.hi == 20 
    assert ae.lo == -1 and ae.hi == 0.4 
    assert af.lo == 7 and af.hi == 14 
    assert ag.lo == 0.5 and ag.hi == 1 
    assert ah.lo == -60 and ah.hi == -20 
    assert cc.lo == -36 and cc.hi == 36 
    assert gc.lo == -3 and gc.hi == 3 	

# Con esto checamos que la funcion igualdad funcione
def test_igualdad():
    x = Intervalo(1,3)
    y = Intervalo(1,3)
    
    # Checamos que x e y sean iguales
    assert x == y

    # Otro test
    z = Intervalo(3)
    assert z == 3

def test_interseccion():
    
    a = Intervalo(1,3)
    b = Intervalo(2,4)
    
    c = a & b
    
    assert c.lo == 2 and c.hi == 3
    d = b & 3
    assert d.lo == 3 and d.hi == 3

def test_negativo():
    
    a = Intervalo(2,5)
    c = -a
    
    assert c.lo == -5 and c.hi == -2

def test_division():
    a = Intervalo(1,2)
    b = Intervalo(1./4,1./2)
    c = a/b
    assert c.lo==2 and c.hi==8
    
    # Otros tests
    d = a/3
    assert d.lo == 1./3 and d.hi==2./3
    d = 3.0/a
    assert d.lo == 3./2 and d.hi == 3.

def test_middle():
    '''
    Se checa que la operacion punto medio funcione
    '''
    num=np.random.uniform(-10.0,10.0)
    num2=np.random.uniform(-10.0,10.0)
    
    #El if siguiente se hace asumiendo que al definir el objeto intervalo incorrectamente
    #este no volteara los valores.
    #if num>num2:
    #    numaux=num2
    #    num2=num
    #    num=numaux
    if num > num2:
        num, num2 = num2, num
    
    a=Intervalo(num,num2)
    c=a.middle()
    
    assert  c==(num+num2)/2
    
def test_radio():
    '''
    Se checa que la operacion radio funcione
    '''
    num=np.random.uniform(-10.0,10.0)
    num2=np.random.uniform(-10.0,10.0)
    
    #if num>num2:
    #    numaux=num2
    #    num2=num
    #    num=numaux
    if num > num2:
        num, num2 = num2, num
    
    a=Intervalo(num,num2)
    c=a.radio()
    
    assert c==(a.hi-a.lo)/2
    
def test_width():
    '''
    Se checa que la operacion width funcione
    '''
    num=np.random.uniform(-10.0,10.0)
    num2=np.random.uniform(-10.0,10.0)
    
    #if num>num2:
    #    numaux=num2
    #    num2=num
    #    num=numaux
    if num > num2:
        num, num2 = num2, num
    
    a=Intervalo(num,num2)
    c=a.width()
    
    assert c==(a.hi-a.lo)  
    
def test_Abs():
    '''
    Se checa que la operacion Abs funcione
    '''
    num=np.random.uniform(-10.0,10.0)
    num2=np.random.uniform(-10.0,10.0)
    
    #if num>num2:
    #    numaux=num2
    #    num2=num
    #    num=numaux
    if num > num2:
        num, num2 = num2, num
    
    a=Intervalo(num,num2)
    c=a.Abs()
    
    assert c==max([abs(a.lo),abs(a.hi)])
