#pip install numpy
#pip3 install numpy

import numpy as np

#listas / vectores / arreglos / arrays 
lista1 = np.array([1, 2, 3, 4, 5])

# lista de dos dimensiones / matriz
lista2 = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])

# Matriz de 3 dimensiones
 # ((#filas, #columnas, #dimensiones), tipo datos) 
img = np.ones((5, 5, 3), np.uint8)
#                       unsigned (sin signo) int de 8 bits  uint8 = byte

#recordemos que 1byte = 8bits 
img[1,2,0] = 150

#  [filas, columnas, dimensiones]
print(img[:, :, 0])
