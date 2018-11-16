from paquete.model import *

lista_jugadores = [Futbolista('Antonio'), MedicoEquipo("Ramon"), PresidenteEquipo("Francisco"), Entrenador("Jose")]

for l in lista_jugadores:
    l.entrenamiento()