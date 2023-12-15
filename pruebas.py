from constraint import *

problem = Problem()

plazas_electricas = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]

# VARIABLES
problem.addVariable('1-TSU-C', plazas_electricas)
problem.addVariable('4-TNU-C', plazas_electricas)
problem.addVariable('7-TNU-C', plazas_electricas)
problem.addVariable('8-TSU-C', plazas_electricas)


vehiculos = ('1-TSU-C', '4-TNU-C', '7-TNU-C', '8-TSU-C')

# RESTRICCIONES
# 1. Todas diferentes
problem.addConstraint(AllDifferentConstraint(), vehiculos)



# 3. Que tenga un lado libre (maniobrabilidad)
def tiene_un_lado_libre(vehiculo):
    izquierda_libre = False
    derecha_libre = False
    print("Vehiculo:" , vehiculo)
    print("Izquierda Libre:" , izquierda_libre)
    print("Derecha Libre:" , derecha_libre)
    # for i in range (len(vehiculos)):
        # print(vehiculo, vehiculo[0], vehiculo[1])
        # print(vehiculos[i], vehiculos[i][0], vehiculos[i][1])
        # print("------------")
        # if ((vehiculo[1] == vehiculos[i][1]) and ((vehiculo[0])-1 == vehiculo[i][0])):
        #     izquierda_libre = False
        # else:
        #     izquierda_libre = True
        
        # if ((vehiculo[1] == vehiculos[i][1]) and ((vehiculo[0])+1 == vehiculo[i][0])):
        #     derecha_libre = False
        # else:
        #     derecha_libre = True

    if (izquierda_libre or derecha_libre):
        return True


# tiene_un_lado_libre('1-TSU-C')


problem.addConstraint(tiene_un_lado_libre, ('1-TSU-C', '4-TNU-C'))
# problem.addConstraint(tiene_un_lado_libre, ('4-TNU-C'))
# problem.addConstraint(tiene_un_lado_libre, ('7-TNU-C'))
# problem.addConstraint(tiene_un_lado_libre, ('8-TSU-C'))




# 2. Una delante de otra
# def delante_de(a, b):
#     if (a[0] == b[0]):
#         if (a[1] > b[1]):
#             return True
#     else:
#         return True

# problem.addConstraint(delante_de, ('1-TSU-C', '4-TNU-C'))
# problem.addConstraint(delante_de, ('1-TSU-C', '7-TNU-C'))
# problem.addConstraint(delante_de, ('8-TSU-C', '4-TNU-C'))
# problem.addConstraint(delante_de, ('8-TSU-C', '7-TNU-C'))

# def delante_de(a, b):
#     if (a[1] > b[1]):
#         texto = a, "está delante de", b
#         return texto
#     if (a[1] < b[1]):
#         texto = b, "está delante de", a
#         return texto
# ambulancia1 = (1, 4)
# ambulancia2 = (1, 6)
# print(delante_de(ambulancia1, ambulancia2))


# SOLUCION
solutions1 = problem.getSolutions()

print("Numero de soluciones:", len(solutions1))
# for solution in solutions1:
    # print(solution)





# EJEMPLO 2
# problem2 = Problem()
# problem2.addVariables(["a", "b"], [1, 2, 3])
# problem2.addConstraint(lambda a, b: b == a+1, ["a", "b"])
# solutions2 = problem2.getSolutions()
# print(solutions2)
