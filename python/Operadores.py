#chr()#-->lleva numero a caracter segun ascii
#ord()#-->lleva caracter a numero segun ascii
#FUNCIONES DE ACTIVACIÓN: ReLu, Sigmoid, Tanh
#ReLu
import math as mt
def ReLu(n):
    return max(0,n)
def sigmoid(n):
    value=1/(1+(mt.e)**(-n))
    return value
def tanh(n):
    senh=(mt.e**n-mt.e**(-n))/2
    cosh=(mt.e**n+mt.e**(-n))/2
    tanh=senh/cosh
    return tanh
x=float(input("Ingrese un valor x a evaluar en las funciones: "))
print(f"Los valores son\n RelU(x) = {ReLu(x)}\n sigmoid(x) = {sigmoid(x)}\n tanh(x) = {tanh(x)}")