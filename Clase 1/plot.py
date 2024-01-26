import matplotlib.pyplot as plt
import random

datos = []

for _ in range(10):
    #                      minino, maximo
    datos.append(random.randint(0,10))

print(datos)

#                (ancho , alto)  en pulgadas (1 pulgada= 80 pixeles)
plt.figure(figsize=(10, 6))


plt.plot(datos)

plt.title("Gráfico de 10 numeros aleatorios")
plt.xlabel("indice")
plt.ylabel("valor")

plt.show()



"""for i in range(1, 101, 1):
    print( "8 x", i, "=", (i*8))"""
