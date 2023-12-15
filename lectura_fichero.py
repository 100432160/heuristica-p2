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
filas = parking_size[0]
columnas = parking_size[1]


# PLAZAS ELECTRICAS
pe = lines[1].split(" ")
plazas_electricas = []
for plaza in pe:
    # Elimina los paréntesis y divide la cadena en una lista de elementos
    elementos = plaza.strip('()').split(',')
    # Convierte cada elemento de la lista en un entero
    plaza = tuple(int(elemento) for elemento in elementos)
    plazas_electricas.append(plaza)


# VEHICULOS
vehiculos = []
for i in range(2, len(lines)):
    vehiculos.append(lines[i])




# print(lines)
# print("Filas:", filas)
# print("Columnas", columnas)
# print("Plazas electricas:", plazas_electricas)
# print(vehiculos)
