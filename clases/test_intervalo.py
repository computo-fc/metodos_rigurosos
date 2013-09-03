# Escribimos funciones con el nombre test_ALGO

from intervalo import Intervalo

def test_adicion():

	a = Intervalo(1, 2)
	b = Intervalo(2, 3)

	c = a + b

	# Quiero checar que c, definido asi, esta bien:

	assert c.min == 3 and c.max == 5
	
def test_interseccioc():
    
    a = Intervalo(1,3)
    b = Intervalo(2,4)
    
    c = a & b
    
    assert c.min == 2 and c.max == 3
