# Ciclos

"""
Los ciclos son estructuras que permiten realizar tareas repetitivas
"""

contador = 0

while contador < 10:                # while se ejecuta siempre y cuando se cumpla la condición
    print("Iteración", contador)
    contador +=1        

print("termina ejecución")

total = 0 #acumulador
num_sumas = 5
contador = 0

while contador < num_sumas:             #suma 5 numeros ingresados por el usario
    num = int(input("Ingresa un numero: "))
    total = total + num
    contador += 1

print("El total de la suma es: ", total)

autorizacion = False                #se inicializa el valor de la condicional del ciclo

while autorizacion == False:        # Mientras la contraseña sea incorrecta el ciclo va a seguir repitienndose
    contraseña = input("Ingesa contraseña: ")
    if contraseña == "123456":
        autorizacion = True
    else:
        print("accesso denegado")

print("Ingreso al sistema")

for numero in [0,1,2,3,4,5,6,7,8,9]:    #recorre los elementos de la lista sin importar el valor de éstos
    print("Iteración", numero)

for numero in [5,6,7,8,9]:    #recorre los elementos de la lista sin importar el valor de éstos
    print("Iteración", numero)

for numero in range(10):    #con range se crea una lista del tamaño 
    print("Iteración", numero)