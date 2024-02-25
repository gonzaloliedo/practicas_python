# Video 10 Tuplas

# Se caracterizan por ser estrucuturas de datos inmutables, por lo tanto se usan para proteger datos. También son más eficientes que las listas.

tupla = ("Juan", 2)

#tupla[0]="Juana" #marca error porque no se puede modificar

#Una opción es convertir la tupla en lista

lista = list(tupla)

print(lista)

lista[0]="Juana"

print(lista)

# de manera recíproca la lista pasa a ser tupla

tupla_modificada = tuple(lista)

print(tupla_modificada)

# Las tuplas tmabién se pueden convertir en conjuntos

set(tupla_modificada)