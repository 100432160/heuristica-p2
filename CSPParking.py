# Importar la libreria
from constraint import *


# Definicion de una variable como nuestro problema
problem = Problem()


# Definicion tamaño del parking
filas = 3
columnas = 3

# Plazas del parking
plazas_parking = []
for i in range(filas):
    for j in range(columnas):
        plazas_parking.append((i+1, j+1))

print("Todas las plazas:", plazas_parking)

# Plazas con electricidad del parking
# plazas_electricas = [(1, 1), (1, 2), (2, 1), (4, 1), (5,1), (5, 2)]
plazas_electricas = [(1, 1), (1, 2), (2, 1), (2, 2), (3,1), (3, 2)]
print("Plazas eléctricas:", plazas_electricas)


# Creacion de las variables
# vehiculos = ('1-TSU-C', '2-TNU-X', '3-TNU-X', '4-TNU-C', '5-TSU-X', '6-TNU-X', '7-TNU-C', '8-TSU-C')
vehiculos = ('1-TNU-X', '2-TNU-X', '3-TNU-X')

def tiene_congelador(vehiculo):
    split_nombre = vehiculo.split("-")
    if (split_nombre[2] == "C"):
        return True
    else:
        return False

for vehiculo in vehiculos:
    necesita_electricidad = tiene_congelador(vehiculo)
    if (necesita_electricidad):
        problem.addVariable(vehiculo, plazas_electricas)
    else:
        problem.addVariable(vehiculo, plazas_parking)



# Creación de las restricciones
# 1. Todo vehículo tiene que tener asignada una plaza y solo una


# 2. Dos vehículos distintos no pueden ocupar la misma plaza
# def notEqual(a, b):
problem.addConstraint(AllDifferentConstraint(), (vehiculos))

# 3. Los vehículos provistos de congelador sólo pueden ocupar plazas con conexión a la red eléctrica


# 4. Un vehículo de tipo TSU no puede tener aparcado por delante, en su misma fila, ningún otro vehículo excepto si este también es TSU
def delante_de(a, b):
    if (a[0] == b[0]):
        if (a[1] > b[1]):
            return True
    else:
        return True
    
def es_TSU(vehiculo):
    split_nombre = vehiculo.split("-")
    if (split_nombre[1] == "TSU"):
        return True
    else:
        return False

for vehiculo in vehiculos:
    if (es_TSU(vehiculo)):
        for otro_vehiculo in vehiculos:
            if ((vehiculo != otro_vehiculo) and (es_TSU(otro_vehiculo) == False)):
                problem.addConstraint(delante_de, (vehiculo, otro_vehiculo))
                # print(vehiculo, "delante_de", otro_vehiculo)



# 5. Por cuestiones de maniobrabilidad dentro del parking todo vehículo debe tener libre una plaza a la izquierda o derecha (mirando en dirección a la salida)
def tiene_un_lado_libre(*vehiculos):
    for vehiculo in vehiculos:
        posicion_izquierda = (vehiculo[0]-1, vehiculo[1])
        posicion_derecha = (vehiculo[0]+1, vehiculo[1])

        derecha_libre = False
        izquierda_libre = False

        izquierda_disponible = True
        derecha_disponible = True
        if (posicion_izquierda not in plazas_parking):
            izquierda_disponible = False
        if (posicion_derecha not in plazas_parking):
            derecha_disponible = False

        for vehiculo_comparacion in vehiculos:
            if vehiculo != vehiculo_comparacion:    # Comparar con los demas vehiculos, no consigo mismo
                izquierda_ocupada = False
                derecha_ocupada = False
                izquierda_disponible = True
                derecha_disponible = True
                
                if (vehiculo[1] == vehiculo_comparacion[1]):    # si estan en la misma columna
                    if (posicion_izquierda[0] == vehiculo_comparacion[0]):
                        izquierda_ocupada = True
                    elif (posicion_derecha[0] == vehiculo_comparacion[0]):
                        derecha_ocupada = True

                if (derecha_disponible and derecha_ocupada == False):
                    derecha_libre = True
                if (izquierda_disponible and izquierda_ocupada == False):
                    izquierda_libre = True
                

                print("---------------------------------------------------")
                print("Comparar", vehiculo, "con", vehiculo_comparacion)
                print("Derecha ocupada:", derecha_ocupada)
                print("Derecha disponible:", derecha_disponible)
                print("Derecha libre:", derecha_libre)
                print("Izquierda ocupada:", izquierda_ocupada)
                print("Izquierda disponible:", izquierda_disponible)
                print("Izquierda libre:", izquierda_libre)

        if (izquierda_libre or derecha_libre):
            return True


problem.addConstraint(tiene_un_lado_libre, vehiculos)




# Recuperacion de las soluciones
print("----------------------------------------------------")
todas_soluciones = problem.getSolutions()

def imprimir_todas_soluciones(soluciones):
	for solucion in soluciones:
		print(solucion)

def imprimir_soluciones(soluciones, numero_soluciones):
	for i in range(numero_soluciones):
		print(soluciones[i])

print("Nº de soluciones:", len(todas_soluciones))
# imprimir_todas_soluciones(todas_soluciones)
imprimir_soluciones(todas_soluciones, 10)