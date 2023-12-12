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
# 1. Todo vehículo tiene que tener asignada una plaza y solo una


# 2. Dos vehículos distintos no pueden ocupar la misma plaza
# def notEqual(a, b):
    
    
problem.addConstraint(AllDifferentConstraint(), ('1-TSU-C', '2-TNU-X', '3-TNU-X', '4-TNU-C', '5-TSU-X', '6-TNU-X', '7-TNU-C', '8-TSU-C'))

# 3. Los vehículos provistos de congelador sólo pueden ocupar plazas con conexión a la red eléctrica


# 4. Un vehículo de tipo TSU no puede tener aparcado por delante, en su misma fila, ningún otro vehículo excepto si este también es TSU


# 5. Por cuestiones de maniobrabilidad dentro del parking todo vehículo debe tener libre una plaza a la izquierda o derecha (mirando en dirección a la salida)



# Recuperacion de las soluciones
print("----------------------------------------------------")
todas_soluciones = problem.getSolutions()

def imprimir_todas_soluciones(soluciones):
	for solucion in soluciones:
		print(solucion)

print("Nº de soluciones:", len(todas_soluciones))
imprimir_todas_soluciones(todas_soluciones)