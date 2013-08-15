# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Tarea 1: Ejercicios de calentamiento con Python

# <markdowncell>

# **REGLAS:**
# 
# - Usa Python para llevar a cabo las tareas. [O julia...]
# 
# - Sí se permite el trabajo colaborativo, y de hecho se fomenta, pero se exige el uso de las neuronas de todos los que colaboren. Se vale entregar una sola tarea por grupo de 2 o (si es necesario) 3 personas.
# 
# - La tarea se entrega como un *notebook* de IPython, y debe incluir notas, comentario y **TODO** lo estéticamente necesario, que lo haga entendible para una tercer persona no involucrada en el curso. 
# 
# - Se recomienda usar una versión nueva de este mismo notebook, reemplazando *[Respuesta aquí] por tu discusión, código, y resultados (en los tipos de celda que convengan, y con el número de ellos que haga falta).
# 
# - Cambia el nombre del notebook para reflejar el nombre que escojan para su grupo de trabajo, e.g. "Tarea-01-profes"
# 
# 

# <markdowncell>

# **1.** Implementa (con Python) el llamado "método Babilónico" para calcular la raíz cuadrada de un 
# número dado, $y$. Este método consiste en la iteración 
# $ x_{n+1} = \frac{1}{2} ( x_n + \frac{y}{x_n}). $
# 
# a. ¿Cuándo se debería terminar la iteracion?
# 
# b. ¿Cuál es la convergencia del método?
# 
# c. Calcula, usando este método, la raíz cuadrada de los números $0$ hasta $10$, en pasos de $0.1$.
# 
# d. ¿Qué sería bueno "poder hacer" --y que aún no hemos aprendido-- con este código para poderlo correr muchas veces sin tener que incluirlo explícitamente?

# <markdowncell>

# *[Respuesta aquí]*

# <markdowncell>

# **2.** Considera la fórmula de recursión $ x_{n+1} = 2 x_n^2 $. 
# 
# ¿Cuál es el valor del iterado $x_{75}$ cuando el valor inicial es $x_0=1-10^{-20}$ ? Compara el resultado 
# numérico obtenido con el que uno esperaría al elevar al cuadrado un número ligeramente menor que 1 un 
# montón de veces... ¿Cuál resultado es el correcto? >Qué necesitarías para verificar esto numéricamente?

# <markdowncell>

# *[Respuesta aquí]*

# <markdowncell>

# **3.** *"Hace muchos muchos años, en un reino muy lejano..."*, se le ocurrió a Arquímedes un método para determinar el valor numérico de $\pi$. El método consiste en considerar dos polígonos regulares de $n$ lados, uno inscrito y otro circunscrito al círculo, y ver cómo el área de estos acota por abajo y arriba el área del círculo. 
# 
# a. Da las cotas (inferior y superior) al área del círculo de radio 1, *al menos* cuando $n=4$, $5$ y $6$ (o sea, las cotas que se obtienen usando los siguientes polígonos regulares:  el cuadrado, el pentágono y el hexágono). 
# 
# [Arquímedes seguramente hizo esto de manera empírica, construyendo los polígonos; para este ejercicio se 
# vale utilizar lo que sabes de geometría y trigonometría.]
# 
# b. ¿Se te ocurre cómo obtener las cotas para $\pi$ usando un polígono regular de $n$ lados?
# 
# (Éste es el **Ejercicio 1.1** del Moore-Kearfortt (2009); la solución que ellos dan me parece que está mal en la cota inferior.)

# <markdowncell>

# *[Respuesta aquí]*

