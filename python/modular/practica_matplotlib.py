import matplotlib
import matplotlib.pyplot as plt
import numpy as np
lista=[1,2,5,7,8,3,1]
plt.plot(lista,'bo-')
lista2=[1,4,6,7,8,9,10]
plt.plot(lista2, lista, 'ro-')
plt.plot([-3,-1,0,4,7], [1,4,6,7,8], 'go-')
plt.axis([-4,8,0,10])#modificando longitudes de los ejes
x=np.linspace(-2,2,500)
y=x**2
y2=x+2
#plt.plot(x,y, 'y--',x,y2,'k:')pero es lo mismo de lo que hacias
plt.figure(figsize=(14,6))#tamaña del gráfico y si los otros gráficos no son del mismo tamaño, lo hace en distintas ventanas
plt.subplot(1,2,1)#esto es para mostrar gráficas en simultáneo
"""plt.plot(x,y, 'y--', label="y=x^2")
plt.plot(x,y2,'k:', label="y=x+1")"""
plt.plot(x,y, 'y--')
plt.subplot(1,2,2)#esto es para mostrar gráficas en simultáneo
plt.plot(x,y2,'k:')
plt.title("Función cuadrática")
plt.xlabel("x", fontsize=14)
plt.ylabel("y=x^2", fontsize=14)
plt.grid(True)#cuadricula habilitada
plt.legend(loc="best")#ubica la leyenda lo mejor posible
plt.show()