import abc

class PersonaEquipo(object):

    def __init__(self):
        self.nombre = ""

    def agregar_nombre(self, nombre):
        self.nombre = nombre
    
    def obtener_nombre(self):
        return self.nombre

class Futbolista(PersonaEquipo):
    def __init___(self):
        super(Futbolista, self).__init__()
        self.posicion_campo = ""

    def entrenar(self):
        print("Formo parte en el entrenamiento")


class Entrenador(PersonaEquipo):
    def __init__(self):
        super(Entrenador, self).__init__()
        self.codigo_entrenador = ""
    
    def entrenar(self):
        print("En el entrenamiento soy el director de la practica")
