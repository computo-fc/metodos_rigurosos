# Escribimos funciones con el nombre test_ALGO

from intervalo import Intervalo

def test_adicion():

	a = Intervalo(1, 2)
	b = Intervalo(2, 3)

	c = a + b

	# Quiero checar que c, definido asi, esta bien:

	assert c.lo == 3 and c.hi == 5
 
 #Aqui se define el test para la resta
 def test_sub():
    a=Intervalo(-11,4)
    b=Intervalo(2,10)
    c=a-b
    assert c.min==-21 and c.max==2
