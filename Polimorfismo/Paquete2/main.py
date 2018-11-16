
from paquete.model import *

lista_jugadores = [Futbolista('Antonio'), MedicoEquipo("Ramon"), PresidenteEquipo("Francisco"), Entrenador("Jóse")]

for l in lista_jugadores:
    l.entrenamiento()