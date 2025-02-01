def aumentar_biblioteca(nuevo_libro):
    books=open("libros.txt")
    libros=books.read().splitlines()
    books.close()
    libros=libros+[nuevo_libro]
    return libros
def primer_libro_leido(libros):
    books=open("libros.txt")
    libros=books.read().splitlines()
    books.close()
    return libros[0]
biblio=aumentar_biblioteca("Cholito en los Andes Mágicos")
print(f"La biblioteca de libros leídos es:\n {biblio}")
print(f"El primer libro que he leído es: {primer_libro_leido(biblio)}")
#TUPLA ES SIMILAR A LISTA, SOLO QUE ES INMUTABLE
datos_personales=("Ana", 30, "Madrid")
def gestionar_informacion(datos_personales):
    nombre, edad, ciudad=datos_personales
    nacimiento=2024-edad
    datos_modificados=(nombre, nacimiento, ciudad)
    return datos_personales,datos_modificados
imprimir1, imprimir2=gestionar_informacion(datos_personales)
print(f"Tupla original: {imprimir1}\nTupla modificada: {imprimir2}")