import time
# IMPORTACIÓN DE LA LIBRERÍA
from constraint import *


#######################################################################################################
# PROCESAR LOS DATOS DEL FICHERO DE PRUEBA
#######################################################################################################
# Abre el archivo en modo lectura
with open('./pruebas/prueba_enunciado.txt', 'r') as file:
    # Lee todas las líneas del archivo y las almacena en una lista
    lines = file.readlines()

file.close()


# Procesar las filas
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")
    lines[i] = lines[i].replace("PE: ", "")


# TAMAÑO DEL  PARKING
parking_size = lines[0].split("x")
filas = int(parking_size[0])
columnas = int(parking_size[1])


# PLAZAS ELECTRICAS
pe = lines[1].split(" ")
plazas_electricas = []
for plaza in pe:
    # Elimina los paréntesis y divide la cadena en una lista de elementos
    elementos = plaza.strip('()').split(',')
    # Convierte cada elemento de la lista en un entero
    plaza = tuple(int(elemento) for elemento in elementos)
    plazas_electricas.append(plaza)


# TODAS LAS PLAZAS DEL PARKING
plazas_parking = []
for i in range(filas):
    for j in range(columnas):
        plazas_parking.append((i+1, j+1))


# VEHICULOS
vehiculos = []
for i in range(2, len(lines)):
    vehiculos.append(lines[i])



# DEFINICIÓN DEL PROBLEMA
problem = Problem()



# Funcion para determinar si un vehiculo tiene congelador o no
def tiene_congelador(vehiculo):
    split_nombre = vehiculo.split("-")
    if (split_nombre[2] == "C"):
        return True
    else:
        return False



#######################################################################################################
# VARIABLES Y DOMINIOS
#######################################################################################################

# El dominio de un vehiculo depende de si tiene congelador o no (RESTRICCIÓN 3)
for vehiculo in vehiculos:
    necesita_electricidad = tiene_congelador(vehiculo)
    if (necesita_electricidad):
        problem.addVariable(vehiculo, plazas_electricas)
    else:
        problem.addVariable(vehiculo, plazas_parking)



#######################################################################################################
# RESTRICCIONES
#######################################################################################################

# RESTRICCION 1. Todo vehículo tiene que tener asignada una plaza y solo una
# Esta restriccion no hace falta ponerla explicitamente puesto que la librería solo asigna un valor a cada variable


# RESTRICCION 2. Dos vehículos distintos no pueden ocupar la misma plaza
problem.addConstraint(AllDifferentConstraint(), (vehiculos))


# RESTRICCION 3. Los vehículos provistos de congelador sólo pueden ocupar plazas con conexión a la red eléctrica
# Esta restriccion se define al limitar el dominio de los vehiculos con congelador a las plazas electricas


# RESTRICCION 4. Un vehículo de tipo TSU no puede tener aparcado por delante, en su misma fila, ningún otro vehículo excepto si este también es TSU
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



# RESTRICCION 5. Por cuestiones de maniobrabilidad dentro del parking todo vehículo debe tener libre una plaza a la izquierda o derecha (mirando en dirección a la salida)
def tiene_un_lado_libre(*vehiculos):
    for vehiculo in vehiculos:
        posicion_izquierda = (vehiculo[0]-1, vehiculo[1])
        posicion_derecha = (vehiculo[0]+1, vehiculo[1])
        derecha_ocupada = False
        izquierda_ocupada = False

        for vehiculo_comparacion in vehiculos:
            if (posicion_izquierda == vehiculo_comparacion):
                izquierda_ocupada = True
            if (posicion_derecha == vehiculo_comparacion):
                derecha_ocupada = True
            
            # Si la plaza derecha y la izquierda estan ocupadas
            if (derecha_ocupada and izquierda_ocupada):
                return False
            # Si la plaza derecha esta ocupada y la izquierda existe
            if (derecha_ocupada and posicion_izquierda[0] < 1):
                return False
            # Si la plaza izquierda esta ocupada y la derecha no existe
            if (izquierda_ocupada and posicion_derecha[0] > filas):
                return False
            
    # Si no se dan las condiciones anteriores, es decir, al menos tiene un lado libre
    return True
                

problem.addConstraint(tiene_un_lado_libre, vehiculos)
                


# Recuperacion de las soluciones
inicio = time.time()
print("----------------------------------------------------")
todas_soluciones = problem.getSolutions()

def imprimir_n_soluciones(soluciones, numero_soluciones):
	for i in range(numero_soluciones):
		print(soluciones[i])

print("Nº de soluciones:", len(todas_soluciones))
imprimir_n_soluciones(todas_soluciones, 10)

final = time.time()
print("Tiempo de ejecución:", round((final-inicio), 2), "segundos")
print("----------------------------------------------------")