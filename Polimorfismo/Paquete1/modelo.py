import abc

# class PersonaEquipo(object):
class PersonaEquipo(metaclass=abc.ABCMeta):
    """
        se define la clases abstracta
    """
    # _metaclass_ = abc.ABCMeta
    
    def _init_(self, nom):
        self.nombre = nom

    @abc.abstractmethod
    def entrenamiento(self):
        pass


# class Futbolista(PersonaEquipo):
#     """
#     """

#     def _init_(self, n):
#         super(Futbolista, self)._init_(n)

#     def entrenamiento(self):
#         print("%s es un futbolista, que participa del entrenamiento" % \
#                 self.nombre)


# class Entrenador(PersonaEquipo):
#     """
#     """

#     def _init_(self, n):
#         super(Entrenador, self)._init_(n)

#     def entrenamiento(self):
#         print("%s es un entrenador, que dirige el entrenamiento" % \
#                 self.nombre)