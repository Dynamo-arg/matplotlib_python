#!/usr/bin/env python
'''
Matplotlib [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.1
Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Sebastian Volpe"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes
import matplotlib.gridspec as gridspec
import mplcursors  # [Opcional cursores]


def ej1():
    # Line Plot
    # Se desea graficar tres funciones en una misma figura
    # en tres gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de x:
    x = list(range(-10, 11, 1))

    # Realizar tres gráficos que representen
    # y1 = x^2 (X al cuadrado)
    # y2 = x^3 (X al cubo)
    # y3 = x^4 (X a la cuarta)
    # Utilizar comprension de listas para generar
    # y1, y2 e y3 basado en los valores de x

    y1 = [i**2 for i in x]
    y2 = [i**3 for i in x]
    y3 = [i**4 for i in x]

    # Esos tres gráficos deben estar colocados
    # en la diposición de 3 filas y 1 columna:
    # ------
    # graf1
    # ------
    # graf2
    # ------
    # graf3
    # ------
    # Utilizar add_subplot para lograr este efecto
    # de "3 filas" "1 columna" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un color distinto
    # a su elección

    gs = gridspec.GridSpec(3, 1)    
    fig = plt.figure("Ejercicio 1")
    ax1 = fig.add_subplot(gs[0, 0])  
    ax2 = fig.add_subplot(gs[1, 0])  
    ax3 = fig.add_subplot(gs[2, 0])  

    ax1.plot(y1, color='darkgreen', label='(X al cuadrado)')
    ax1.set_facecolor('whitesmoke')
    ax1.legend()
    ax1.grid('solid')

    ax2.plot(y2, color='r', label='(X al cubo)')
    ax2.set_facecolor('grey')
    ax2.legend()
    ax2.grid('solid')

    ax3.plot(y3, color='blue', label='(X a la cuarta)')
    ax3.set_facecolor('white')
    ax3.legend()
    ax3.grid('solid')


    plt.show()


def ej2():
    # Scatter Plot
    # Se desea graficar dos funciones en una misma figura
    # en dos gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de x:
    x = np.arange(0, 4*np.pi, 0.1)

    # Realizar dos gráficos que representen
    # y1 = sin(x)
    # y2 = cos(x)
    # Utilizar los métodos de Numpy para calcular
    # "y1" y "y2" basado en los valores de x

    y1 = [np.sin(i) for i in x]
    y2 = [np.cos(i) for i in x]
    
    # Esos dos gráficos deben estar colocados
    # en la diposición de 1 fila y 2 columnas:
    # ------
    #  graf1 | graf2
    # ------
    # Utilizar add_subplot para lograr este efecto
    # de "1 fila" "2 columnas" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un mark distinto
    # a su elección.

    gs = gridspec.GridSpec(1, 2)    
    fig = plt.figure("Ejercicio 2")
    ax1 = fig.add_subplot(gs[0, 0])  
    ax2 = fig.add_subplot(gs[0, 1])  

    ax1.plot(x,y1, color='darkgreen', marker='+', label='y1 = sin(x)')
    ax1.set_facecolor('whitesmoke')
    ax1.legend()
    ax1.grid('solid')

    ax2.plot(x,y2, color='r', marker='1',label='y1 = cos(x)')
    ax2.set_facecolor('white')
    ax2.legend()
    ax2.grid('solid')

    plt.show()




def ej3():
    # Bar Plot
    # Generar un gráfico de barras simple a partir
    # de la siguiente información:

    lenguajes = ['Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp']
    performance = [10, 8, 6, 4, 2, 1]

    # Realizar un gráfico de barras en donde se pueda ver el uso
    # de cada lenguaje, se debe utilizar los labels "lenguajes"
    # como valor del eje X

    # Se debe colocar título al gráfico.
    # Se debe cambiar la grilla y el fondo a su elección.

    width = 0.2  # Tamaño de la barra
    fig = plt.figure("Ejercicio 3")
    fig.suptitle('Lenguajes', fontsize=16)
    ax = fig.add_subplot()

    ax.bar(lenguajes, performance, 
            width=0.5, color=['red', 'blue', 'purple', 'green', 'grey', 'gold'],
            label='Lenguajes')
    ax.set_facecolor('white')
    ax.legend()
    ax.set_xticks(lenguajes)
    ax.set_xticklabels(lenguajes)
    plt.show()


def ej4():
    # Pie Plot
    # Se desea realizar un gráfico de torta con la siguiente
    # información acerca del % de uso de lenguajes en nuevos
    # programadores
    uso_lenguajes = {'Python': 29.9, 'Javascript': 19.1,
                     'Go': 16.2, 'Java': 10.5, 'C++': 10.2,
                     'C#': 8.2, 'C': 5.9
                     }


    # El gráfico debe tener usar como label las keys del diccionario,
    # debe usar como datos los values del diccionario
    # Se desea resaltar (explode) el dato de Python
    # Se desea mostrar en el gráfico los porcentajes de c/u
    # Se debe colocar un título al gráfico

    fig = plt.figure()
    fig.suptitle('Lenjuages Compraracion', fontsize=16)
    ax = fig.add_subplot()

    explode = (0.1, 0, 0 ,0 ,0 ,0 ,0)  # solo resaltar el consumo de carne

    ax.pie(uso_lenguajes.values(), labels=uso_lenguajes.keys(),
           explode=explode, autopct='%1.1f%%', shadow=True, startangle=90
           )
    ax.axis('equal')
    plt.show()




def ej5():
    # Uso de múltiples líneas en un mismo gráfico (axes)
    # En el siguiente ejemplo generaremos una señal senoidal
    # haciendo uso solamente de comprension de listas
    step = 0.1
    sample_size = 100
    signal = [{'X': i*step, 'Y': math.sin(i*step)} for i in range(sample_size)]

    # Se generó una lista de diccionarios con dos columnas "X" e "Y"
    # que corresponden a los valores de nuestra señal senoidal.
    # Se pide usar comprensión de listas para generar las dos listas
    # por separado de los valoresde "X" e "Y" para poder utilizar
    # el line plot y observar la señal

    signal_x =  [x.get('X', '') for x in signal]
    
    signal_y = [x.get('Y', '') for x in signal]

    # plot(signal_x, signal_y)

    gs = gridspec.GridSpec(1, 2)     
    fig = plt.figure()
    ax1 = fig.add_subplot(gs[0, 0]) 
    ax2 = fig.add_subplot(gs[0, 1])  

    ax1.plot(signal_x, color='darkgreen', label='Señal X')
    ax1.set_facecolor('whitesmoke')
    ax1.legend()
    ax1.grid('solid')

    ax2.plot(signal_y, color='darkblue', label='Señal Y')
    ax2.set_facecolor('whitesmoke')
    ax2.legend()
    ax2.grid('solid')
    plt.show()



    # Ahora que han visto la señal senoidal en su gráfico, se desea
    # que generen otras dos listas de "X" e "Y" pero filtradas por
    # el valor de "Y". Solamente se debe completar la lista
    # con aquellos valores de "Y" cuyo valor absoluto (abs)
    # supere 0.7

    filter_signal_x = [data for data in signal_x if data > abs(0.7)]
    filter_signal_y = [data for data in signal_y if data > abs(0.7)]
    
    # Graficar juntas ambos conjuntos de listas y observar
    # el resultado. Graficar filter como scatter plot

    # plot(signal_x, signal_y)
    # scatter(filter_signal_x, filter_signal_y)

    gs = gridspec.GridSpec(1, 2)     
    fig = plt.figure()
    ax1 = fig.add_subplot(gs[0, 0])  
    ax2 = fig.add_subplot(gs[0, 1])  
    fig.suptitle('Filtrados por Valor Absoluto mas 0.7"', fontsize=14)


    ax1.scatter([i for i in filter_signal_y],filter_signal_y ,c='darkred', marker='^',  label='Filtrado Y')
    ax1.legend()
    ax1.grid()
    ax1.set_facecolor('whitesmoke')

    ax2.scatter([i for i in filter_signal_x],filter_signal_x ,c='black', marker='+',  label='Filtrado X')
    ax2.legend()
    ax2.grid()
    ax2.set_facecolor('whitesmoke')


    plt.show()

    # Pueden ver el concepto y la utilidad de
    # realizar un gráfico encima de otro para filtrar datos?


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()