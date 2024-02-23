#Video 9 Conjuntos /sets

"""
Operaciones básicas sobre conjuntos
"""

nombres2020 = {"Juan", "Pedro",  "Luis", "Pedro"}
nombres2021 = {"Luis", "María", "Rosa"}

print(nombres2020)      #Podemos observar que solo se imprimen los datos no repetidos 
print(nombres2021)

#si se le añade con .add() un elemento repetido, el conjunto no se inmuta y siguen apareciendo los mismos valores

nombres2021.add("Luis")
nombres2021.add("Jose") #valor no repetido

print(nombres2021) #también es de notar que el orden de los valores no está garantizado

#con el método de .remove() se pueden eliminar valores de los conjuntos

nombres2021.remove("Jose")

#para observar los nombres que se han utilizado tanto en 2021 como en 2022 se usa la UNIÓN de ambos  conjuntos

nombres = nombres2021.union(nombres2020)

print(nombres)

#para ver los nombres que se repiten en ambos años se usa la INTERSECCIÓN de ambos conjuntos de datos

nombres_coincidentes = nombres2020.intersection(nombres2021)

print(nombres_coincidentes)

# se puede restar la intersección de la unión de ambos conjuntos. Dicho de  otra manera se puede eliminar el valor que repite en ambas listas del conjunto de nombres de ambos años

print(nombres.difference(nombres_coincidentes))

# para verificar que un conjunto contiene a otro se usa .issubset()
print(nombres2020.issubset(nombres)) # aqui preguntamos si los nombres usados en 2020 está en el conjunto de nombres (lo cual es verdadero)

print(nombres.issubset(nombres2020)) # como nombres no es conjunto de los nombres usados en 2020 inidica que es falso

print(nombres.issuperset(nombres2020)) # el conjunto de nombres del 2020 al estar contenido dentro del conjunto de nombres, es verdadero.