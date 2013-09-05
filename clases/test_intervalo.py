# -*- coding: utf-8 -*-
# Escribimos funciones con el nombre test_ALGO

from intervalo import Intervalo

def test_adicion():

	a = Intervalo(1, 2)
	b = Intervalo(2, 3)

	c = a + b

	# Quiero checar que c, definido asi, esta bien:

	assert c.hi == 3 and c.lo == 5

# Con esto checamos que la funcion igualdad funcione
	
def test_igualdad():
    x = Intervalo(1,3)
    y = Intervalo(1,3)
    
    # Checamos que x e y sean iguales
    assert x == y
