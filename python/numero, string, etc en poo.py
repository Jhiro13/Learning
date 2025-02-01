img=3+4j
print(img.real)
print(img.imag)
#problema1
class SimuladorPrestamo:
    def __init__(self, detalles_prestamo):
        self.tasa_anual=detalles_prestamo.imag
        self.tasa_mensual=detalles_prestamo.imag/1200
        self.años_presatamo=30
        self.numero_pagos=self.años_presatamo*12
        self.entrada=detalles_prestamo.real
        self.precio_vivienda=300000
        self.prestamo=self.precio_vivienda-self.entrada
        self.cuota_mensual=None
    def calcular_pago_total(self):
        self.cuota_mensual=self.prestamo*(self.tasa_mensual*(1+self.tasa_mensual)**self.numero_pagos)/((1+self.tasa_mensual)**self.numero_pagos-1)
        return
    def mostrar_resultado(self):
        print("-----Simulación Hipoteca-----")
        print(f"Para una vivienda de {self.precio_vivienda} euros, aportando una entrada de {self.entrada} euros y con una tasa de interés del {self.tasa_anual}% anual durante {self.años_presatamo} años:")
        print(f"Cuota mensual a pagar: {self.cuota_mensual} euros")
        print("-----Fin de la Simulación-----")
details=SimuladorPrestamo(50000+2.5j)
details.calcular_pago_total()
details.mostrar_resultado()
#Strings
texto="cHiNg Es KbRo"
print(texto.capitalize())#solo vuelve mayuscula la primera letra
print(texto.upper())#a mayusculas
print(texto.lower())#a minusculas
print(texto.title())#a titulo
print(texto.swapcase())#alterna las mayus y minus
texto1="aoo boo coo boo"
print(texto1.count("oo"))#te cuenta las veces que se repite una subcadena
print(texto1.find("boo"))#devuelve el indice donde se encuentra la subcadena
print(texto1.rfind("boo"))#al reves te busca
texto2="abc123"
texto3="abc$123"
texto2.isalnum()#detecta si es alfanumerico o no
texto3.isdigit()#si todos son numeros
text="Hola Mundo"
print(text.center(20))#lo centra 20 especios
print(text.ljust(20))
print(text.rjust(20))
text.lstrip()#te borra todos los saltos de linea y espaciados por la izquierda y te deja texto puro
text.rstrip()
text.strip()#quita los de izquierda y derecha
#text.join() pa concatenar
print(text.replace(" ",""))#reemplaza caractere
text.zfill(32)#completea los 32 bits con 0 la izquierda
#problema2
class GeneradorNombresUsuario:
    def __init__(self, nombre, apellido, año):
        self.nombre=nombre
        self.apellido=apellido
        self.año=año
        self.usuario=self.generar_nombre_usuario()
    def generar_nombre_usuario(self):
        return self.nombre.lower()+self.apellido.upper()+str(self.año)
    def _validar_nombre_usuario(self):
        return len(self.usuario)>=8 and self.usuario[-4:].isdigit()
    def mostrar_nombre_usuario(self):
        if self._validar_nombre_usuario():
            print(f"Nombre de usuario generado: {self.usuario}")
        else:
            print("El nombre de usuario no cumple con los criterios de validación")
usuario1=GeneradorNombresUsuario("SanTIAgo","HerNANDeZ",1994)
usuario1.generar_nombre_usuario()
usuario1.mostrar_nombre_usuario()
#LISTAS
lista=["azul","verde","rojo"]
lista.append("amarillo")#añade un unico valor
print(lista)
lista.extend(["morado","marron","dorado"])#recibe una lista y extiende la actual
print(lista)
lista.remove("rojo")
print(lista)
lista.reverse()
print(lista)
lista.pop()#quita el ultimo elemento de la lista y te lo devuelve
lista1=lista.copy()#copia la lista
lista.clear()#Te limpia la lista
list=['azul','verde','rojo']
list.index('verde')#te da el indice
list.count('rojo')#te cuenta elementos
#problem 3
class SistemaCalificaciones: 
    def __init__(self, calificaciones):
        self.calificaciones=calificaciones
    def añadir_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)
    def mostrar_calificaciones(self):
        for i in range (len(self.calificaciones)):
            print(f"{self.calificaciones[i]}")
    def calificacion_promedio(self):
        if len(self.calificaciones)>0:
            return sum(self.calificaciones)/len(self.calificaciones)
        else:
            print("NO SE INGRESARON CALIFICACIONES")
    def ordenar_calificaciones(self):
        return self.calificaciones.sort()
notas=[]
cal1=SistemaCalificaciones(notas)
cal1.añadir_calificacion(8)
cal1.añadir_calificacion(9.5)
cal1.añadir_calificacion(7)
cal1.añadir_calificacion(10)
print("Calificaicones originales:")
cal1.mostrar_calificaciones()
print(f"Promedio: {cal1.calificacion_promedio()}")
cal1.ordenar_calificaciones()
print("Calificaciones ordenandas:")
cal1.mostrar_calificaciones()
#TUPLAS
class AnalisisVentas:
    def __init__(self, datos_ventas):
        self.datos_ventas=datos_ventas
    def venta_maxima(self):
        m=max(self.datos_ventas)
        ind=self.datos_ventas.index(m)
        return ind, m
    def venta_minima(self):
        mi=min(self.datos_ventas)
        indm=self.datos_ventas.index(mi)
        return indm, mi
    def frecuencia_venta(self, venta):
        return self.datos_ventas.count(venta)
ventas=(100, 150, 150, 50, 250, 300, 100, 350, 200, 200, 150)
analisisv1=AnalisisVentas(ventas)
print(f"La venta máxima tiene el índice {analisisv1.venta_maxima()[0]} y es {analisisv1.venta_maxima()[1]}")
print(f"La venta mínima tiene el índice {analisisv1.venta_minima()[0]} y es {analisisv1.venta_minima()[1]}")
print(f"La frecuencia de la venta por un valor de 200 es {analisisv1.frecuencia_venta(200)}")
#SETS
miset1={"azul", "rojo", "verde"}
miset2={"morado", "rojo", "amarillo"}
miset3={"verde"}
print(miset1.intersection(miset2))
print(miset1.union(miset2))
print(miset1.issubset(miset2))
print(miset3.issubset(miset1))
print(miset1.symmetric_difference(miset2))
class GestionAsistencia:
    def __init__(self):
        self.asistentes_actividad_A=set({})
        self.asistentes_actividad_B=set({})
    def añadir_asistente(self, actividad, estudiante):
        if actividad=="A":
            self.asistentes_actividad_A.add(estudiante)
        elif actividad=="B":
            self.asistentes_actividad_B.add(estudiante)
    def asistencia_total(self):
        asistentes=self.asistentes_actividad_A.union(self.asistentes_actividad_B)
        return asistentes
    def asistencia_comun(self):
        comunes=self.asistentes_actividad_A.intersection(self.asistentes_actividad_B)
        return comunes
    def diferencia_actividad_A(self):
        soloA=self.asistentes_actividad_A.difference(self.asistentes_actividad_B)
        return soloA
    def diferencia_actividad_B(self):
        soloB=self.asistentes_actividad_B.difference(self.asistentes_actividad_A)
        return soloB
asis=GestionAsistencia()
asis.añadir_asistente("A", "Ana")
asis.añadir_asistente("A", "Juan")
print(f"Asitentes actividad A: {asis.asistentes_actividad_A}")
asis.añadir_asistente("B", "Ana")
asis.añadir_asistente("B", "Luis")
print(f"Asistentes actividad B: {asis.asistentes_actividad_B}")
print(f"Asistencia total: {asis.asistencia_total()}")
print(f"Asistencia común: {asis.asistencia_comun()}")
print(f"Diferencia actividad A: {asis.diferencia_actividad_A()}")
print(f"Diferencia actividad B: {asis.diferencia_actividad_B()}")
#Diccionarios
diccionario={
    "key1":1,
    "key2":2
}
diccionario.update({"key1":10})
print(diccionario)
diccionario.update({"key3":13})
print(diccionario)
diccionario.pop("key1")
print(diccionario)
diccionario.clear()
diccionario.values()#te da los valores nms
diccionario.keys()#te da las claves nms
diccionario.items()#para recorrer diccionarios
#problema
class GestionInventario:
    def __init__(self):
        self.inventario={}
    def añadir_productos(self, producto, cantidad):
        if producto in self.inventario:
            self.inventario[producto]+=cantidad
        else:
            self.inventario.update({producto:cantidad})
    def eliminar_producto(self, producto):
        self.inventario.pop(producto)
    def consultar_producto(self, producto):
        if producto in (self.inventario):
            return self.inventario.get(producto)
        else:
            print("Producto no existe en el inventario")
    def mostrar_inventario(self):
        for producto, cantidad in self.inventario.items():
            print(f"{producto}: {cantidad}")
inven1=GestionInventario()
inven1.añadir_productos("Manzanas",10)
inven1.añadir_productos("Peras",5)
inven1.añadir_productos("Manzanas",5)
print(f"Consultar manzanas: {inven1.consultar_producto("Manzanas")}")
print("---Inventario---")
inven1.mostrar_inventario()
print("----------------")
inven1.eliminar_producto(("Peras"))
print("Inventario después de eliminar Peras: ")
print("---Inventario---")
inven1.mostrar_inventario()
print("----------------")