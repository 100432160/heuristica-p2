from constraint import *

problem = Problem()

plazas_electricas = [(1, 1), (1, 2), (2, 1), (2, 2)]

# VARIABLES
problem.addVariable('1-TSU-C', plazas_electricas)
problem.addVariable('4-TNU-C', plazas_electricas)
problem.addVariable('7-TNU-C', plazas_electricas)
problem.addVariable('8-TSU-C', plazas_electricas)




# RESTRICCIONES
# 1. Todas diferentes
problem.addConstraint(AllDifferentConstraint(), ('1-TSU-C', '4-TNU-C', '7-TNU-C', '8-TSU-C'))


# 2. Una delante de otra
def delante_de(a, b):
    if (a[0] == b[0]):
        if (a[1] > b[1]):
            return True
    else:
        return True

problem.addConstraint(delante_de, ('1-TSU-C', '4-TNU-C'))
problem.addConstraint(delante_de, ('1-TSU-C', '7-TNU-C'))
problem.addConstraint(delante_de, ('8-TSU-C', '4-TNU-C'))
problem.addConstraint(delante_de, ('8-TSU-C', '7-TNU-C'))

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
for solution in solutions1:
    print(solution)





# EJEMPLO 2
# problem2 = Problem()
# problem2.addVariables(["a", "b"], [1, 2, 3])
# problem2.addConstraint(lambda a, b: b == a+1, ["a", "b"])
# solutions2 = problem2.getSolutions()
# print(solutions2)
