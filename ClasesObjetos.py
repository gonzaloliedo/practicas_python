#video 1 Clases y objetos
class Tragamonedas:                 # es una buena práctica iniciar con mayúscula el nombre de la clase
    def __init__(self, id, premio): #inicilizar constructor
        self.id = id                 #inicializar atributo
        self.premio = premio
                                    # para crear una instancia -> tragamonedas = Tragamonedas()