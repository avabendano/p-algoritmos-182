class PersonaEquipo(object):

    def _init_(self):
        self.nombre = ""

    def agregar_nombre(self, nombre):
        self.nombre = nombre
    
    def obtener_nombre(self):
        return self.nombre

    def entrenar(self):
        pass

class Futbolista(PersonaEquipo):
    def _init__(self):
        super(Futbolista, self)._init_()
        self.posicion_campo = ""

    def entrenar(self):
        print("Formo parte en el entrenamiento")


class Entrenador(PersonaEquipo):
    def _init_(self):
        super(Entrenador, self)._init_()
        self.codigo_entrenador = ""
    
    def entrenar(self):
        print("En el entrenamiento soy el director de la practica")