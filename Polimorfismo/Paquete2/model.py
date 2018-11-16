import abc


class PersonaEquipo(metaclass=abc.ABCMeta):
    """
        se define la clases abstracta
    """

    def _init_(self, nom):
        self.nombre = nom

    @abc.abstractmethod
    def entrenamiento(self):
        pass


class Futbolista(PersonaEquipo):
    """
    """

    def _init_(self, n):
        super(Futbolista, self)._init_(n)

    def entrenamiento(self):
        print("Yo %s, futbolista, hago participa en el entrenamiento." %
              self.nombre)


class Entrenador(PersonaEquipo):
    """
    """

    def _init_(self, n):
        super(Entrenador, self)._init_(n)
        self.codigo_entrenado = ""

    def entrenamiento(self):
        print("Yo %s, entrenador, soy el director del entrenamiento." % self.nombre)


class MedicoEquipo(PersonaEquipo):
    def _init_(self, n):
        super(MedicoEquipo, self)._init_(n)
        self.titulo = ""

    def entrenamiento(self):
        print("Yo %s, medico, atiendo a los jugadores en el entrenamiento." %
              self.nombre)


class PresidenteEquipo(PersonaEquipo):
    def _init_(self, n):
        super(PresidenteEquipo, self)._init_(n)
        self.numero_propiedades = ""

    def entrenamiento(self):
        print("Yo %s, presidente, pongo le dinero para el entrenamiento." %
              self.nombre)