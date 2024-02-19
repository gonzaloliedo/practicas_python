#video 1 Clases y objetos

from random import randint #importar librería que permite obtener números pseudoaleatorios

class Tragamonedas:                 # es una buena práctica iniciar con mayúscula el nombre de la clase
    def __init__(self, id, premio): #inicilizar constructor __init__ solo se  usa cuando son inherentes a la clase objeto
        self.id = id                 #inicializar atributo
        self.premio = premio
        self.monedas = 0
        self.jackpots = 0

    def __str__(self):                      #sobrecarga del método
        return "ID: " + str(self.id) + "-Premio: " + str(self.premio)
    
    def __eq__(self, otro):
        return self.monedas == otro.monedas #compara si un atributo es igual(eq=equal) al de otra instancia, en este caso monedas.
    
    def __lt__(self, otro):
        return self.monedas < otro.monedas #compara si un atributo es menor(lt=less than) al de otra instancia, en este caso monedas.
    
    def __gt__(self, otro):
        return self.monedas > otro.monedas #compara si un atributo es mayor(gt=greater than) al de otra instancia, en este caso monedas.

    def jugar(self):                    #método de dominio
        self.monedas += 1               #cada vez que usas el tragamonedas tienes que usar una moneda
        numeros= randint(0, 9), randint(0, 9), randint(0, 9) #devuelve una tupla de tres números simulando el resultado del tragamoneda
        mensaje = ""                    #inicializas mensaje para mostrar al usario cada vez que usas el trgamonedas
        if numeros [0]==numeros[1]==numeros[2]: #condicional que permite determinar el resultado del tragamonedas
            self.jackpots += 1                  #si ganas incrementa las veces que se ha ganado el jackpot
            mensaje = "Felicidades Ganaste %0.2f" %self.premio
        else:                                   # en caso de perder se muestra un mensaje ad hoc
            mensaje = "Sigue intentando"
        
        return numeros, mensaje
                                  
#se crean dos instancias de la clase Tragamonedas

tragamonedas = Tragamonedas(1, 1000.00)  # para crear una instancia -> tragamonedas = Tragamonedas()
tragamonedas2 = Tragamonedas(2, 200.00)

for i in range(100):                    #simular 100 juegos en las dos máquinas
    print(tragamonedas.jugar())
    print(tragamonedas2.jugar())

print(tragamonedas.jackpots)        #se verifica cuantas veces se ha ganado en las máquinas
print(tragamonedas2.jackpots)

print(tragamonedas)                 #se observa que con la sobrecarga del método __str__ ya no imprime la dirección de memoria
print(tragamonedas2)

# a pesar de que dos instancias tengan los mismos valores en sus atributos no son iguales, esto se puede verificar con el método id(), 
# para comparar si los atributos entre dos instancias se puedes usar la sobrecargas del método __eq__ de "equal" o igual, __lt__ "less than" o menor que y __gt__ "greater than"  
print(tragamonedas == tragamonedas2)
print(id(tragamonedas))
print(id(tragamonedas2))