# video 4 Recursividad con Python

"""
Impresión de números en cuenta atrás
"""

def recursivo(n):
    if n == 0:          #condicional que valida que el conteo llegó a cero el conteo
        print(n)
    else:
        print(n)
        recursivo(n-1)  #Si el conteo todavía no llega a cero se vuelve a llamar la función solo que disminuyendo en 1 el valor de entrada

recursivo(6)

"""
Impresión de una operación factorial
"""

def factorial(n):
    if n == 0 or n == 1: # 0! = 1! = 1
         return 1
    resultado=1  # Se inicializa el valor el valor en 1

    for i in range(2, n+1):
         resultado = resultado * i #se actualiza el valor de resultado multiplicando el anterior por el ínidice i
    return resultado
     

def factorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial_recursivo(n-1) #se vuelve a llamar a la función 
    
for i in range(6):
    print(i, factorial(i), factorial_recursivo(i))

from time import perf_counter

inicio = perf_counter()     # se hace la comparación de tiempo de ejecución entre una funcion iterativa y una recursiva

for i in range(1000000):
    factorial(100)

fin= perf_counter()

print("Tiempo de ejecución Iterativo: %0.4f" %(fin-inicio))

inicio = perf_counter()     # se hace la comparación de tiempo de ejecución entre una funcion iterativa y una recursiva

for i in range(1000000):
    factorial_recursivo(100)

fin= perf_counter()

print("Tiempo de ejecución Recursivo: %0.4f" %(fin-inicio))

#Una de las desventajas de la programación recursiva es que es más lenta aunque se reduzca la cantidad de líneas de código

"""
Se obtuvo que el tiempo de ejecución de la función iterativa fue de 4.3787s y de la función recursiva fue de 12.0670s. Casi el triple.
"""