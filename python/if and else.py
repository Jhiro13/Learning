def recomendar_pelicula(genero, edad):
    if genero=="accion" and edad>=13:
        return "Deadpool"
    elif genero=="accion" and edad<13:
        return "Regreso al futuro"
    elif genero=="comedia":
        return "Aterriza como puedas"
    else:
        return "Explorar otros géneros"
u_genero="accion"
u_edad=26
print(f"Teniendo en cuenta tu edad ({u_edad}) y tu género favorito ({u_genero}), te recomiendo la siguiente película: {recomendar_pelicula(u_genero, u_edad)}")
#FOR
lista_iterador=iter([1,2,3])#--> da un iterador
next(lista_iterador)#--> te devuelve 1 a 1 los valores de la lista
def añadir_tarea(tarea):
    archivo=open("tareas.txt")
    tareas=archivo.read().splitlines()
    archivo.close()
    tareas=tareas+[tarea]
    return tareas
def gestionar_tareas(lista_tareas):
    n=0
    for i in lista_tareas:
        print(f"{n+1}. {lista_tareas[n]}\n")
        n+=1
    print(f"Hay {n} tareas pendientes de realizar")
print("Tareas pendientes de realizar:\n")
gestionar_tareas(añadir_tarea("Pagar la factura del internet."))
#WHILE
def mover_ascensor(piso_actual, piso_deseado):
    while piso_actual!=piso_deseado:
        if piso_actual>piso_deseado:
            print(f"Bajando al piso {piso_deseado}. Piso actual: {piso_actual}")
            piso_actual-=1
        else:
            print(f"Subiendo al piso {piso_deseado}. Piso actual: {piso_actual}")
            piso_actual+=1
    print(f"Piso {piso_deseado} alcanzado")
mover_ascensor(2,6)
#BREAK      CONTINUE    PASS
def simulador_alarma(tiempo_total):
    segundo_actual=0
    while segundo_actual!=tiempo_total:
        segundo_actual+=1
        if segundo_actual%10==0:
            print(f"Omitiendo alarma en segundo {segundo_actual}")
            continue
        print(f"Alarma activada, segundo actual: {segundo_actual}")
        if segundo_actual==tiempo_total:
            break
    print(f"Alarma desactivada a los {segundo_actual} segundos")
simulador_alarma(21)    
        