# Importar la libreria
from constraint import *


# Definicion de una variable como nuestro problema
problem = Problem()


# Definicion tamaño del parking
filas = 5
columnas = 6

# Plazas del parking
plazas_parking = []
for i in range(filas):
    for j in range(columnas):
        plazas_parking.append((i+1, j+1))

print("Todas las plazas:", plazas_parking)

# Plazas con electricidad del parking
plazas_electricas = [(1, 1), (1, 2), (2, 1), (4, 1), (5, 1), (5, 2)]
print("Plazas eléctricas:", plazas_electricas)


# Creacion de las variables
problem.addVariable('1-TSU-C', plazas_electricas)
problem.addVariable('2-TNU-X', plazas_parking)
problem.addVariable('3-TNU-X', plazas_parking)
problem.addVariable('4-TNU-C', plazas_electricas)
problem.addVariable('5-TSU-X', plazas_parking)
problem.addVariable('6-TNU-X', plazas_parking)
problem.addVariable('7-TNU-C', plazas_electricas)
problem.addVariable('8-TSU-C', plazas_electricas)


# Creación de las restricciones