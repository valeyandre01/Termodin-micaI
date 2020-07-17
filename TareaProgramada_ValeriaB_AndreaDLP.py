import random
import numpy as np
import time
from matplotlib import pyplot as plt
global s

###matriz original de ceros:###
###a esta se le agregará en el centro la de unos de 10x10###
cafenegro = np.zeros((100, 100))
###matriz para subdividir los pasos guardados###
###(mejor explicación en la función dividir###
cafe = np.zeros((100, 100))


###función de crea la matriz en el estado 0###
def initialize():
    i = 45
    while i < 55:
        j = 45
        while j < 55:
            cafenegro[i][j] = 1
            j = j + 1
        i = i + 1


###función para graficar la matriz###
def paint(matrix):
    # Se crea el gráfico
    plt.style.use('grayscale')
    plt.matshow(matrix)
    # Se coloca el título del gráfico
    plt.title("Grilla")
    plt.axis('off')
    plt.show()


###función que realiza el random walk y guarda cada iteración###
def executeg(iterations):

    #abre o crea un txt llamado prueba
    doc = open("prueba.txt", "w")

    #llama a la función que crea el estado 0
    initialize()

    cont = 0

    while cont < iterations:
        i2 = 0
        while i2 < 100:
            j2 = 0
            while j2 < 100:
                if cafenegro[i2][j2] == 1:

                    num = random.randint(1, 4)
                    if num == 1 and i2 > 0:

                        if (cafenegro[i2 - 1][j2] != 1) and (cafenegro[i2 - 1][j2] != 2):

                            # arriba

                            cafenegro[i2][j2] = 0

                            cafenegro[i2 - 1][j2] = 1

                            j2 = j2 + 1

                        else:
                            j2 = j2 + 1

                    elif num == 2 and j2 > 0:

                        if (cafenegro[i2][j2 - 1] != 1) and (cafenegro[i2][j2 - 1] != 2):
                            # izquierda

                            cafenegro[i2][j2] = 0

                            cafenegro[i2][j2 - 1] = 1

                            j2 = j2 + 1

                        else:
                            j2 = j2

                    elif num == 3 and i2 < 99:

                        if (cafenegro[i2 + 1][j2] != 1) and (cafenegro[i2 + 1][j2] != 2):
                            # abajo

                            cafenegro[i2][j2] = 0

                            cafenegro[i2 + 1][j2] = 2

                            j2 = j2 + 1

                        else:
                            j2 = j2

                    elif num == 4 and j2 < 99:

                        if (cafenegro[i2][j2 + 1] != 1) and (cafenegro[i2][j2 + 1] != 2):
                            # derecha

                            cafenegro[i2][j2] = 0

                            cafenegro[i2][j2 + 1] = 2

                            j2 = j2 + 1
                        else:
                            j2 = j2

                elif cafenegro[i2][j2] == 2:
                    cafenegro[i2][j2] = 1
                    j2 = j2 + 1

                else:
                    j2 = j2 + 1

            i2 = i2 + 1

        #guarda como una lista todas las iteraciones
        for fila in cafenegro:
            np.savetxt(doc, fila)

        cont += 1

    doc.close()

    paint(cafenegro)


###función para calcular la entropía de un estado###
def entropia(matrix):
    global s
    s = 0
    estado = 0
    i = 0
    j = 0
    limi = i + 10
    limj = j + 10
    prob = []

    while estado < 100:
        cant = 0

        #corre el estado
        while i < limi:
            j = limj - 10

            while j < limj:

                if matrix[i][j] == 1:
                    #calcula cantidad de 1 por estado
                    cant = cant + 1
                j = j + 1
            i = i + 1
        pi = (cant / 100)
        prob.append(pi)

        if limj < 100:
            i = limi - 10
            limj = limj + 10

        else:
            j = 0
            limj = j + 10
            i = limi
            limi = limi + 10

        estado = estado + 1

    for p in prob:
        if p > 0:
            formula = abs(p * np.log(p))
            s = s + formula


###función que grafica entropía###
def paints(y):
    plt.plot(y)
    #título
    plt.title("Evolución de la entropía del sistema")
    #titulos de ejes
    plt.ylabel("entropía")
    plt.xlabel("tiempo (pasos)")
    plt.show()


###función que recopila los datos en una matriz grande y lo va dividiendo por iteración###
def dividir(iterations):
    sentropia = []
    datos = np.loadtxt("prueba.txt").reshape((100 * iterations), 100)
    cont = 0
    i2 = 0
    limitei = i2 + 100

    while cont < iterations:
        i = 0

        while i2 < limitei:
            j = 0

            while j < 100:
                cafe[i][j] = datos[i2][j]
                j = j + 1

            i = i + 1
            i2 = i2 + 1

        #llama a la función de entropía y la guarda en una lista
        entropia(cafe)
        global s
        sentropia.append(s)
        i2 = limitei
        limitei = limitei + 100
        cont = cont + 1

    paints(sentropia)


###ejecución, ambos parámetros deben ser iguales###
executeg('CAMBIE POR CANTIDAD DE ITERACIONES DESEADAS')

dividir('CAMBIE POR CANTIDAD DE ITERACIONES DESEADAS')
