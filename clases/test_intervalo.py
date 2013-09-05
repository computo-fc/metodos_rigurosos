# Escribimos funciones con el nombre test_ALGO

from intervalo import *

import numpy as np

def test_adicion():
    a = Intervalo(1, 2)
    b = Intervalo(2, 3)
    c = a + b

	# Quiero checar que c, definido asi, esta bien:
    assert c.lo == 3 and c.hi == 5

def test_middle():
    '''
    Se checa que la operacion punto medio funcione
    '''
    num=np.random.uniform(-10.0,10.0)
    num2=np.random.uniform(-10.0,10.0)
    
    #El if siguiente se hace asumiendo que al definir el objeto intervalo incorrectamente
    #este no volteara los valores.
    if num>num2:
        numaux=num2
        num2=num
        num=numaux
        
    a=Intervalo(num,num2)
    c=a.middle()
    
    assert  c==(num+num2)/2
    
def test_radio():
    '''
    Se checa que la operacion radio funcione
    '''
    num=np.random.uniform(-10.0,10.0)
    num2=np.random.uniform(-10.0,10.0)
    
    if num>num2:
        numaux=num2
        num2=num
        num=numaux
        
    a=Intervalo(num,num2)
    c=a.radio()
    
    assert c==(a.hi-a.lo)/2
    
def test_width():
    '''
    Se checa que la operacion width funcione
    '''
    num=np.random.uniform(-10.0,10.0)
    num2=np.random.uniform(-10.0,10.0)
    
    if num>num2:
        numaux=num2
        num2=num
        num=numaux
        
    a=Intervalo(num,num2)
    c=a.width()
    
    assert c==(a.hi-a.lo)  
    
def test_Abs():
    '''
    Se checa que la operacion Abs funcione
    '''
    num=np.random.uniform(-10.0,10.0)
    num2=np.random.uniform(-10.0,10.0)
    
    if num>num2:
        numaux=num2
        num2=num
        num=numaux
        
    a=Intervalo(num,num2)
    c=a.Abs()
    
    assert c==max([abs(a.lo),abs(a.hi)])
        
