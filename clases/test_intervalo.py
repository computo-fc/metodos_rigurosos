# Escribimos funciones con el nombre test_ALGO

from intervalo import Intervalo

def test_adicion():

	a = Intervalo(1, 2)
	b = Intervalo(2, 3)

	c = a + b

	# Quiero checar que c, definido asi, esta bien:

	assert c.lo == 3 and c.hi == 5
	
def test_interseccioc():
    
    a = Intervalo(1,3)
    b = Intervalo(2,4)
    
    c = a & b
    
    assert c.lo == 2 and c.hi == 3
    
def test_negativo():
    
    a = Intervalo(2,5)
    c = -a
    
    assert c.lo == -5 and c.hi == -2
