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
    '''Test < de intervalos'''

    a=Intervalo(-1,1)
    b=Intervalo(0,1)
    c=Intervalo(1,2)
    d=Intervalo(2,3)

    assert (a<a) == False
    assert (a<b) == False and (b<a) == False
    assert (b<c) == False and (c<b) == False
    assert (b<d) == True  and (d<b) == False
    assert (c<d) == False and (d<c) == False

def test_comparacion_gt():
    '''Test > de intervalos'''

    a=Intervalo(-1,1)
    b=Intervalo(0,1)
    c=Intervalo(1,2)
    d=Intervalo(2,3)
    
    assert (a>a) == False
    assert (a>b) == False and (b>a) == False
    assert (b>c) == False and (c>b) == False
    assert (b>d) == False and (d>b) == True
    assert (c>d) == False and (d>c) == False
    
def test_comparacion_le():
    '''Test <= de intervalos'''
    a=Intervalo(-1,1)
    b=Intervalo(0,1)
    c=Intervalo(1,2)
    d=Intervalo(2,3)

    assert (a<=a) == True
    assert (a<=b) == True and (b<=a) == False
    assert (b<=c) == True and (c<=b) == False
    assert (b<=d) == True and (d<=b) == False
    assert (c<=d) == True and (d<=c) == False

def test_comparacion_ge():
    '''Test >= de intervalos'''
    a=Intervalo(-1,1)
    b=Intervalo(0,1)
    c=Intervalo(1,2)
    d=Intervalo(2,3)

    assert (a>=a) == True
    assert (a>=b) == False and (b>=a) == True
    assert (b>=c) == False and (c>=b) == True
    assert (b>=d) == False and (d>=b) == True
    assert (c>=d) == False and (d>=c) == True
