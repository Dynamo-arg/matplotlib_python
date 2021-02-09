#!/usr/bin/env python
'''
Matplotlib [Python]
Ejercicios de profundización
---------------------------
Autor: Sebastian Volpe
Version: 1.2

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.2"

import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes
import matplotlib.gridspec as gridspec
import mplcursors
import csv


'''
NOTA PARA TODOS LOS EJERCICIOS

Para la resolución de todos los problemas utilizará
el dataset "ventas.csv".

Desde ahora los de datos los generará c/u
con Numpy o comprensión de listas o ambos, queda
a su elección en cada caso. Si quiere usar Numpy
para todo, puede abrir el archivo directamente con Numpy
y trabajar sin pasar por listas o diccionarios.

TIP: Para abrir el archivo CSV con Numpy y que el header no
     quede mezclado con los datos utilizar:
     data = np.genfromtxt('ventas.csv', delimiter=',')
     # Borro la fila 0 del header, los nombres de las columnas
     data = data[1:,:]

NO están permitidos los bucles en la realización de estos ejercicios.

Descripción del dataset "ventas.csv"
- Este dataset contiene el importe facturado por un local
  en la venta de sus productos dividido en 4 categorías
- Se contabiliza lo vendido por categória al cerrar el día,
  el dataset está ordenado por mes y día
- El dataset contiene 3 meses (genéricos) de 30 días c/u

'''


def ej1():
    print('Comenzamos a divertirnos!')

    '''
    Para comenzar a calentar en el uso del dataset se lo solicita
    que grafique la evolución de la facturación de la categoría alimentos
    para el primer mes (mes 1) de facturación.
    Realice un line plot con los datos de facturación de alimentos del mes 1
    Deberá poder observar la evolución de ventas(y) vs días(x)

    TIP:
    1) Para aquellos que utilicen listas siempre primero deberan
    emprezar filtrando el dataset en una lista de diccionarios que
    posee solo las filas y columnas que a están buscando.
    En este caso todas las filas cuyo mes = 1 y solo la columan
    de día(x) y de alimentos(y).
    Una vez que tiene esa lista de dccionarios reducida a la información
    de interés, debe volver a utilizar comprensión de listas para separar
    los datos de los días(x) y de los alimentos(y)

    2) Para aquellos que utilicen Numpy, si transformaron su CSV en Numpy
    les debería haber quedado una matriz de 6 columnas y de 90 filas
    (recordar sacar la primera fila que es el header)
    mes | dia | alimentos | bazar | limpieza | electrodomesticos
    Luego si quisieramos acceder a solo la columna de los dias (col=1)
    podemos utilizar slicing de Numpy:
    dias = dataset[:, 1]
    ¿Cómo puedo obtener las filas solo del primer mes?
    Aplicando mask de Numpy:
    mes_1 --> col = 0
    filas_mes_1 = dataset[:, 0] == 1
    Obtengo solos los datos del mes uno
    mes_1 = dataset[filas_mes_1, :]

    x --> dias
    Obtengo solo los dias del mes1 de alimentos
    x = dataset[filas_mes_1, 1]
    o tambien puede usar
    x = mes_1[:, 1]

    y --> alimentos
    Obtengo solo los alimentos del mes1 de alimentos
    y = dataset[filas_mes_1, 2]
    o tambien puede usar
    y = mes_1[:, 2]

    '''
    dataset = np.genfromtxt('ventas.csv', delimiter=',')
    dataset = dataset[1:,:]
    filas_mes_1 = dataset[:, 0] == 1
    x = dataset[filas_mes_1, :]
    y = x[:, 2]
    
    fig = plt.figure()
    fig.suptitle('Ventas Enero Alimentos', fontsize=14)
    ax = fig.add_subplot()

    ax.plot(y, c='darkred', marker='^', ms=10, label='Ventas Enero')
    ax.legend()
    ax.grid()
    ax.set_facecolor('whitesmoke')
    plt.show()


def ej2():
    print('Comenzamos a ponernos serios!')

    '''
    Queremos visualizar como ver la tendencia de venta de los alimentos
    a lo largo de todo el año.
    Para eso queremos utilizar el método "np.diff" para obtener la diferencia
    día a día de lo vendido.

    Se debe poder primero discriminar las ventas por la categoría Alimentos,
    1) en el caso de usar listas se debe generar una lista de solo
       ventas de aliementos de todo el año.
    2) En el caso de usar numpy no hace falta generar una lista/array aparte,
       pero si le resulta comodo puede hacerlo.

    Luego que tienen discriminadas las ventas por alimento aplicar el método
    np.diff
    tendencia = np.diff(mis ventas de alimentos)

    Graficar el valor obtenido con un Line Plot

    NOTA: Importante!, en este caso no disponen facilmente del eje "X" de diff,
    para simplificar el caso solamente graficar la variable "tendencia"
    plot(tendencia)

    '''
    dataset = np.genfromtxt('ventas.csv', delimiter=',')
    dias = dataset[:, 2]
    tendencia = np.diff(dias)
    
    fig = plt.figure()
    fig.suptitle('Evolucion Ventas Alimentos Anual "X"', fontsize=14)
    ax = fig.add_subplot()

    ax.plot(tendencia, c='r', marker='.', ms=10, label='Evolucion')
    ax.legend()
    ax.grid()
    ax.set_facecolor('whitesmoke')
    plt.show()


def ej3():
    print("Buscando la tendencia")

    '''
    Si observa el dataset, los electrodomésticos no siempre
    tienen facturación al finalizar el día.
    Deseamos que generen una nueva lista/array/columna
    en la cual coloquen un "1" si ese día se vendió electrodomésticos
    o un "0" sino se vendio nada (facturación = 0).
    Luego graficar utilizando Line Plot esta nueva lista/array/columna
    para visualizar la tendencia de cuantos días consecutivos hay
    ventas de electrodomésticos.

    '''
    dataset = np.genfromtxt('ventas.csv', delimiter=',')
    dataset = dataset[1:,:]

    electro = dataset[:, 5] == 0

    ventas_electro = [1 if x == False else 0 for x in electro]

    fig = plt.figure()
    fig.suptitle('Ventas Concretadas Electrodomesticos"', fontsize=14)
    ax = fig.add_subplot()

    ax.plot(ventas_electro, c='c', marker='.', ms=10, label='Evolucion')
    ax.legend()
    ax.grid()
    ax.set_facecolor('whitesmoke')
    plt.show()



def ej4():
    print("Exprimiendo los datos")

    '''
    Obtener la facturación total (la suma total en los 3 meses)
    de cada categória por separado. Nos debe quedar el total
    facturado en alimentos, en bazar, en limpieza y en
    electrodomesticos por separado (son 4 valores)

    TIP:
    1) para los que usan listas, para poder obtener estos
    valores primero deberan generar una lista de cada categoría,
    para luego poder aplicar operaciones como sum.
    2) Para los que usan numpy pueden usar directamente np.sum
    y especificando el axis=0 estarán haciendo la suma total de la columna

    Con la información obtenida realizar un Pie Plot
    para visualizar que categoría facturó más en lo que va
    del año
    '''
    dataset = np.genfromtxt('ventas.csv', delimiter=',')
    dataset = dataset[1:,:]

    Alimentos = np.sum(dataset[:,2])
    Bazar = np.sum(dataset[:,3])
    Limpieza = np.sum(dataset[:,4])
    Electrodomesticos = np.sum(dataset[:,5])

    y = np.array([Alimentos, Bazar, Limpieza, Electrodomesticos])
    mylabels = ["Alimentos", "Bazar", "Limpieza", "Electrodomesticos"]
    myexplode = [0, 0, 0, 0.2]

    fig = plt.figure()
    fig.suptitle('Ventas Anuales por producto', fontsize=16)
    plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
    plt.show() 


def ej5():
    print("Ahora sí! buena suerte :)")

    '''
    Ahora que ya hemos jugado un poco con nuestro dataset,
    queremos realizar 3 gráficos de columnas en una misma figura
    Cada gráfico de columnas deben tener 4 columnas que representan
    el total vendido de cada categoría al final del mes.
    Para poder hacer este ejercicio deben obtener primero
    total facturado por categoria por mes (deben filtrar por mes)
    Es parecido a lo realizado en el ejercicio anterior pero en vez
    de todo el año es la suma total por mes por categoría.

    Siendo que son 4 categorías y 3 meses, deben obtener al final
    12 valores, con esos 12 valores construir 3 listas/arrays
    para poder mostrar los 3 gráficos de columnas

    BONUS Track: Si están cancheros y aún quedan energías para practicar,
    les proponemos que en vez de realizar 3 gráficos de columnas separados
    realicen uno solo y agrupen la información utilizando gráfico de barras
    apilados o agrupados (a su elección)
    '''

    dataset = np.genfromtxt('ventas.csv', delimiter=',')
    dataset = dataset[1:,:]

    # Cargo las 12 varialbles necesarias:
    alimentos_mes_1 = [dataset[x,2] for x in range(0,90) if dataset[x,0] == 1]
    alimentos_mes_2 = [dataset[x,2] for x in range(0,90) if dataset[x,0] == 2]
    alimentos_mes_3 = [dataset[x,2] for x in range(0,90) if dataset[x,0] == 3]
    bazar_mes_1 = [dataset[x,3] for x in range(0,90) if dataset[x,0] == 1]
    bazar_mes_2 = [dataset[x,3] for x in range(0,90) if dataset[x,0] == 2]
    bazar_mes_3 = [dataset[x,3] for x in range(0,90) if dataset[x,0] == 3]
    limpieza_mes_1 = [dataset[x,4] for x in range(0,90) if dataset[x,0] == 1]
    limpieza_mes_2 = [dataset[x,4] for x in range(0,90) if dataset[x,0] == 2]
    limpieza_mes_3 = [dataset[x,4] for x in range(0,90) if dataset[x,0] == 3]
    electro_mes_1 = [dataset[x,5] for x in range(0,90) if dataset[x,0] == 1]
    electro_mes_2 = [dataset[x,5] for x in range(0,90) if dataset[x,0] == 2]
    electro_mes_3 = [dataset[x,5] for x in range(0,90) if dataset[x,0] == 3]

    # Los juntos todos en 3 Array

    mes1 = [
        np.sum(alimentos_mes_1), 
        np.sum(bazar_mes_1),
        np.sum(limpieza_mes_1),
        np.sum(electro_mes_1)]

    mes2 = [
        np.sum(alimentos_mes_2), 
        np.sum(bazar_mes_2),
        np.sum(limpieza_mes_2),
        np.sum(electro_mes_2)]

    mes3 = [
        np.sum(alimentos_mes_3), 
        np.sum(bazar_mes_3),
        np.sum(limpieza_mes_3),
        np.sum(electro_mes_3)]


    productos = ['Alimentos', 'Bazar', 'Limpieza', 'Electros']

    fig, (ax1, ax2, ax3) = plt.subplots(1,3)
    fig.suptitle('Ventas Mensuales x Productos:')

    ax1.bar(productos,mes1, color = 'r')
    ax2.bar(productos,mes2, color = 'g')
    ax3.bar(productos,mes3, color = 'c')
    ax1.set_xlabel('MES 1')
    ax2.set_xlabel('MES 2')
    ax3.set_xlabel('MES 3')
    ax1.set_ylabel('CANTIDAD')
            
    plt.show()


if __name__ == '__main__':
    print("Ejercicios de práctica")
    # ej1()
    # ej2()
    # ej3()
    # ej4()
    ej5()
