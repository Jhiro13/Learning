from IPython.display import clear_output
#Lo importado de esta libreria permite limpiar la pantalla cada que se ejecute
f=6
c=7
def crear_tabla(filas,columnas):
    tablero=[None]*filas
    for i in range (filas):
        tablero[i]=["."]*columnas
    return tablero
table=crear_tabla(f,c)
def mostrar_tablero(tablero):
    for num in range(len(tablero[0])):
        print(f"{num}", end="  ")
    for i in tablero:
        print("")
        for j in i:
            print(f"{j}", end="  ")
def introducir_ficha(tablero,c,color):
    if c >= len(tablero[0]) or c < 0:
        print("Error. Fuera de Rango...")
        return
    elif tablero[0][c] != '.':
        print("Columna llena de Fichas...")
    else:
        for fila in range (len(tablero)-1,-1,-1):
            if tablero[fila][c] == '.':
                tablero[fila][c]=color
                return tablero
def revisar_filas(tablero,color):
    nfilas=len(tablero)
    ncolums=len(tablero[0])
    for r in range (nfilas):
        for c in range (ncolums-3):
            if tablero[r][c] == color and tablero[r][c+1] == color and tablero[r][c+2] == color and tablero[r][c+3] == color:
                return True
def revisar_columnas(tablero,color):
    nfilas=len(tablero)
    ncolums=len(tablero[0])
    for c in range (ncolums):
        for r in range (nfilas-3):
            if tablero[r][c] == color and tablero[r+1][c] == color and tablero[r+2][c] == color and tablero[r+3][c] == color:
                return True
def revisar_diagonal_derecha(tablero,color):
    nfilas=len(tablero)
    ncolums=len(tablero[0])
    for c in range (ncolums-3):
        for r in range (nfilas-1,2,-1):
            if tablero[r][c] == color and tablero[r-1][c+1] == color and tablero[r-2][c+2] == color and tablero[r-3][c+3] == color:
                return True
def revisar_diagonal_izquierda(tablero,color):
    nfilas=len(tablero)
    ncolums=len(tablero[0])
    for c in range (ncolums-1,2,-1):
        for r in range (nfilas-1,2,-1):
            if tablero[r][c] == color and tablero[r-1][c-1] == color and tablero[r-2][c-2] == color and tablero[r-3][c-3] == color:
                return True
def comprobar_ganador(tablero,color):
    return revisar_filas(tablero,color) or revisar_columnas(tablero,color) or revisar_diagonal_derecha(tablero,color) or revisar_diagonal_izquierda(tablero,color)
turno='X'
sig_turno='O'
while True:
    turno=sig_turno
    mostrar_tablero(table)
    if turno == 'X':
        columna=int(input("Turno de X: "))
        sig_turno='O'
    elif turno == 'O':
        columna=int(input("Turno de O: "))
        sig_turno='X'
    introducir_ficha(table,columna,turno)
    clear_output(wait=False)
    if comprobar_ganador(table,turno):
        print(f"Ganador el jugador: {turno}\n")
        mostrar_tablero(table)
        break