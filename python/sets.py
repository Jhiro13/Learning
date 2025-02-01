lista=[1,1,1,2,3,4,5,5,6,6]
mi_set=set(lista)
print(mi_set)#elimina los duplicados y es inaccesible
#fset ya lo vuelve inmutable (frozenset)
fset=frozenset({"azul", "verde", "amarillo"})
print(fset)#no hay orden gaa
#EJERCICIO
coleccion = [
    "Mona Lisa", "El Grito", "Mona Lisa", "La Noche Estrellada",
    "Las Meninas", "Guernica", "La Última Cena", "La Creación de Adán",
    "La Persistencia de la Memoria", "La Libertad guiando al pueblo",
    "El Beso", "Nacimiento de Venus", "El Jardín de las Delicias",
    "La Joven de la Perla", "El David",
    "Los Girasoles", "La Gran Ola de Kanagawa",
    "La Ronda Nocturna", "American Gothic",
    "Los Jugadores de Cartas", "La Noche Estrellada",
    "La Última Cena", "Guernica", "Las Meninas",
    "La Persistencia de la Memoria", "Mona Lisa"
]
def revisar_coleccion(coleccion):
    n_lista=list(set(coleccion))
    return n_lista
print(f"Colección antes de la revisión: {coleccion}\nColección después de la revisión: {revisar_coleccion(coleccion)}")
#NONETYPE: objeto vacio