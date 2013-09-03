# Escribimos funciones con el nombre test_ALGO

#from intervalo import Intervalo

def test_igualdad():
    x = Intervalo(1,3)
    y = Intervalo(1,3)
    
    # Checamos que x e y sean iguales
    assert x == y
