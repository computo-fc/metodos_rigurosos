# -*- coding: utf-8 -*- 
# Escribimos funciones con el nombre test_ALGO

from intervalo_luis  import *

import numpy as np

def test_adicion():
    a = Intervalo(1, 2)
    b = Intervalo(2, 3)
    c = a + b

    # Quiero checar que c, definido asi, esta bien:
    assert c.lo == 3 and c.hi == 5

def test_comparacion_lt():
    '''Se verifica el test < de intervalos'''
	#Faltan los casos interesantes cuando se 
	#comparan con un intervalo que tenga 
	# al cero.
    a=Intervalo(2,3)
    b=Intervalo(0,1)
    c=Intervalo(-1,1)

    assert (a<b) == False and (b<a) == True
    assert (a<c)

def test_comparacion_gt():
    '''Se verifica el test > de intervalos'''
    a=Intervalo(2,3)
    b=Intervalo(0,1)
    assert (a>b) == True and (b>a) == False
    
    
    
