# -*- coding: utf-8 -*- 

# Escribimos funciones con el nombre test_ALGO
from sympy import mpmath as mp
from intervalo import *

import numpy as np

def TwoReals():
    """
    Funcion auxiliar para el test de intervalos con intervalos aleatorios
    """
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
        
    return num,num2

def test_adicion():
    num,num2=TwoReals()
    numb,numb2=TwoReals()
    a = Intervalo(num, num2)
    b = Intervalo(numb, numb2)
    c = a + b

    # Quiero checar que c, definido asi, esta bien:
    assert c.lo == num+numb and c.hi == num2+numb2

def test_resta():
    #Test para las restas siguiendo la idea de Neftalí.
    
    num=np.random.uniform(-10.0,10.0)
    num2=np.random.uniform(-10.0,10.0)
    num3=np.random.uniform(-10.0,10.0)
    num4=np.random.uniform(-10.0,10.0)
    
    if num > num2:
        num, num2 = num2, num
    if num3 > num4:
        num3, num4 = num4, num3
    
    a=Intervalo(num,num2)
    b=Intervalo(num3,num4)
    
    c = a - b
    d = 3.0 - a
    e = a - 3.0

    assert c.lo== (num - num4) and c.hi== (num2 - num3)
    assert d.lo== (3.0 - num2) and d.hi== (3.0 - num)
    assert e.lo== (num - 3.0) and e.hi== (num2 - 3.0)
    
def test_multiplicacion():
    """
    Se verfica la multiplicacion entre intervalos
    """
    # Test de la multiplicacion (Laura y Leon)
    num,num2=TwoReals()
    numb,numb2=TwoReals()
    a = Intervalo(num, num2)
    b = Intervalo(numb, numb2)
    c = a*b
    #a = Intervalo(1, 2)
    #b = Intervalo(3, 4)
    #c = Intervalo(6,-6)
    #d = Intervalo(0,10)
    #e = Intervalo(-0.5,0.2)
    #f = 7
    #g = 0.5
    #h = Intervalo(-30,-20)
    #ab = a*b
    #ac = a*c
    #ad = a*d
    #ae = a*e
    #af = a*f
    #ag = a*g
    #ah = a*h
    #cc = c*c
    #gc = g*c
    # Quiero checar que todas la multiplicaciones de arriba, definidas asi, estan bien:
    #assert ab.lo == 3 and ab.hi == 8 
    #assert ac.lo == -12 and ac.hi == 12 
    #assert ad.lo == 0 and ad.hi == 20 
    #assert ae.lo == -1 and ae.hi == 0.4 
    #assert af.lo == 7 and af.hi == 14 
    #assert ag.lo == 0.5 and ag.hi == 1 
    #assert ah.lo == -60 and ah.hi == -20 
    #assert cc.lo == -36 and cc.hi == 36 
    #assert gc.lo == -3 and gc.hi == 3 	
    S=[num*numb,num*numb2,num2*numb,num2*numb2]
    assert c.lo==min(S) and c.hi==max(S)

# Con esto checamos que la funcion igualdad funcione
def test_igualdad():
    """
    Se verifica la igualdad entre intervalos
    """
    num,num2=TwoReals()
    x = Intervalo(num,num2)
    y = Intervalo(num,num2)
    
    # Checamos que x e y sean iguales
    assert x == y

    # Otro test
    z = Intervalo(num)
    assert z == num

def test_interseccion():
    """
    Test de interseccion de intervalos
    """
    num,num2=TwoReals()
    numb,numb2=TwoReals()
    #Se eligen los intervalos de la siguiente manera para evitar
    #que de la interseccion resulte un conjunto vacio
    a = Intervalo(min(num,numb), max(num2,numb))
    b = Intervalo(max(num,numb),max(num2,numb2))
    
    #a = Intervalo(1,3)
    #b = Intervalo(2,4)
    
    c = a & b
    
    assert c.lo == max(a.lo,b.lo) and c.hi == min(a.hi,b.hi)
    d = a & a.middle()
    assert d.lo == a.middle() and d.hi == a.middle()

def test_negativo():
    
    a = Intervalo(2,5)
    c = -a
    
    assert c.lo == -5 and c.hi == -2
    
def test_reciproco():
    
    a = Intervalo(10, 12)
    b = Intervalo(-1, 5)
    c = Intervalo(0)
   
    assert a.reciprocal().lo == 1.0/12 and a.reciprocal().hi == 1.0/10
    
    try:
        b.reciprocal()
    except ZeroDivisionError:
        assert True
    
    try:
        c.reciprocal()
    except ZeroDivisionError:
        assert True

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
    """
    Se checa que la operacion punto medio funcione
    """
    num,num2=TwoReals()
    a=Intervalo(num,num2)
    c=a.middle()
    
    assert  c==(num+num2)/2
    
def test_radio():
    """
    Se checa que la operacion radio funcione
    """
    num,num2=TwoReals()
    
    a=Intervalo(num,num2)
    c=a.radio()
    
    assert c==(a.hi-a.lo)/2
    
def test_width():
    """
    Se checa que la operacion width funcione
    """
    num,num2=TwoReals()
    
    a=Intervalo(num,num2)
    c=a.width()
    
    assert c==(a.hi-a.lo)  
    
def test_Abs():
    """
    Se checa que la operacion Abs funcione
    """
    num,num2=TwoReals()
    
    a=Intervalo(num,num2)
    c=a.abs()
    
    assert c==max([abs(a.lo),abs(a.hi)])


def test_sub():
    a=Intervalo(-11,4)
    b=Intervalo(2,10)
    c=a-b
    assert c.lo==-21 and c.hi==2


def test_comparacion_lt():
    """Test < de intervalos."""

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
    """Test > de intervalos."""

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
    """Test <= de intervalos."""
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
    """Test >= de intervalos."""
    a=Intervalo(-1,1)
    b=Intervalo(0,1)
    c=Intervalo(1,2)
    d=Intervalo(2,3)

    assert (a>=a) == True
    assert (a>=b) == False and (b>=a) == True
    assert (b>=c) == False and (c>=b) == True
    assert (b>=d) == False and (d>=b) == True
    assert (c>=d) == False and (d>=c) == True

def test_hull():
    num=np.random.uniform(-10.0,10.0,[10])
    num2=np.random.uniform(-10.0,10.0,[10])
    a = Intervalo(num[0],num2[0])
    b=[]
    for i in range(len(num)):
      a = Intervalo.hull(a,Intervalo(num[i],num2[i]))
      b.append(Intervalo(num[i],num2[i]))
    ##plot_intevalo(b)
    assert (a.lo==min(min(num),min(num2))) & (a.hi==max(max(num),max(num2)))

##def plot_intevalo(a,y=0):
##    from matplotlib import pyplot as plt
##    mins=[]
##    maxs=[]
##    for i in a:
##      y=y+0.05
##      col=np.random.uniform(0.0,1.0,[3])
##      plt.figure(1)
##      plt.hlines(y,i.lo,i.hi,colors=tuple(col),linewidths=1.5)
##      plt.vlines(i.lo,y-0.03,y+0.03,colors=tuple(col),linewidths=1.5)
##      plt.vlines(i.hi,y-0.03,y+0.03,colors=tuple(col),linewidths=1.5)
##      mins.append(i.lo)
##      maxs.append(i.hi)
##      
##    plt.xlim(min(mins)-1.0,max(maxs)+1.0)
##    #plt.ylim(y-0.5,y+0.5)
##    return plt.show()

def test_exp():
    """
    Se verifica que la operacion exponancial funcione
    """
    num, num2 = TwoReals()

    a = mp.exp(num)
    b = mp.exp(num2)
    c = Intervalo(num, num2).exp()
    assert a == c.lo and b == c.hi

def test_log():
    """
    Se verifica que la operacion logaritmo funcione.
    """

    num, num2 = TwoReals()
    

    try:
      a = mp.log(num)
      b = mp.log(num2)
      c=Intervalo(num, num2).log()
      assert a == c.lo and b == c.hi 
    except: 
      if num2 < 0:
	pass
	#Debemos checar que se de el ValueError
      elif num < 0 and num2 >= 0:
	a = mp.log(num + np.abs(num))
	b = mp.log(num2)
	c=Intervalo(num, num2).log()
	assert a == c.lo and b == c.hi 
      
    
