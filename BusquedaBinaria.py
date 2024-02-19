#video 3 Busqueda Binaria: Programación Iterativa y recursiva

# Para hacer búsqueda binaria se requiere que la lista esté ordenada previamente.
# Consiste en evaluar los valores situados en la mitad de la lista en comparación con el valor objetivo. Si no se localiza el valor deseado, 
# se ajustan los extremos de la búsqueda y se recalcula el valor medio. Este proceso se repite hasta encontrar la coincidencia buscada, 
# optimizando la búsqueda de manera iterativa hasta converger.

def busqueda_iterativa(lista, dato): #caso iterativo
    bajo = 0
    alto =len(lista) - 1
    centro = (bajo + alto)//2   # se ocupa una división entera porque no hay indices con decimales

    while bajo <= alto:
        if lista[centro] == dato: #si encuentra el valor objetivo regresa el indice de la lista
            return centro
        elif lista[centro] < dato: #si el valor centro es menor al objetivo, el valor centro es el nuevo valor bajo
            bajo = centro + 1
        else:
            alto = centro - 1       #si el valor centro es mayor al objetivo , el calor centro es el nuevo valor alto
        centro = (bajo + alto)//2 #se actualiza el nuevo centro
    return -1 #No existe el elemento en la lista

lista = [11,12,13,14,15,16,17]

#el caso recursivo es más pesado en términos de eficiencia
def busqueda_recursiva(lista, bajo, alto, dato): #caso recursivo
    if bajo > alto:
        return -1 # No existe
    centro = (bajo + alto)//2
    if lista[centro] == dato:
        return centro
    elif lista[centro] < dato:
        return busqueda_recursiva(lista, centro+1, alto, dato) #se vuelve a calcular el centro ingresando el valor de centro como atributo "bajo"
    else:
        return busqueda_recursiva(lista, bajo, centro-1, dato) #se vuelve a calcular el centro ingresando el valor de centro como atributo "alto"

for i in range(10,19):
    print(i, busqueda_iterativa(lista,i))
    print(i, busqueda_recursiva(lista, 0, len(lista)-1, i))