import abc


class PersonaEquipo(metaclass=abc.ABCMeta):
    """
        se define la clases abstracta
    """

    def __init__(self, nom):
        self.nombre = nom

    @abc.abstractmethod
    def entrenamiento(self):
        pass


class Futbolista(PersonaEquipo):
    """
    """

    def __init__(self, n):
        super(Futbolista, self).__init__(n)

    def entrenamiento(self):
        print("Yo %s, futbolista, hago participa en el entrenamiento." %
              self.nombre)


class Entrenador(PersonaEquipo):
    """
    """

    def __init__(self, n):
        super(Entrenador, self).__init__(n)
        self.codigo_entrenado = ""

    def entrenamiento(self):
        print("Yo %s, entrenador, soy el director del entrenamiento." % self.nombre)


class MedicoEquipo(PersonaEquipo):
    def __init__(self, n):
        super(MedicoEquipo, self).__init__(n)
        self.titulo = ""

    def entrenamiento(self):
        print("Yo %s, medico, atiendo a los jugadores en el entrenamiento." %
              self.nombre)


class PresidenteEquipo(PersonaEquipo):
    def __init__(self, n):
        super(PresidenteEquipo, self).__init__(n)
        self.numero_propiedades = ""

    def entrenamiento(self):
        print("Yo %s, presidente, pongo le dinero para el entrenamiento." %
              self.nombre)
