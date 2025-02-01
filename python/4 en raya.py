f=6
c=7
def crear_tabla(filas,columnas):
    tablero=[None]*filas
    for i in range (filas):
        tablero[i]=["."]*columnas
    return tablero
table=crear_tabla(f,c)
def ver_tablero(tablero):
    for i in range (len(tablero)):
        print(f"{str(tablero[i])}\n")
ver_tablero(table)
def introducir_ficha(tablero,filas,columnas):
    col=int(input("ingrese columna (1 a 7): "))
    n=0
    for i in range (filas-1,-1,-1):
        if (tablero[i][col-1]=="." and n<1):
            tablero[i][col-1]=input("ingrese ficha (X/O): ")
            n+=1
        else:
            continue
    return tablero
def revisar_columnas(tablero,filas,columnas):
    for j in range (0,columnas):
        for i in range (filas-4,-1,-1):
            if ((tablero[i][j]==tablero[i+1][j]==tablero[i+2][j]==tablero[i+3][j]=="X") or (tablero[i][j]==tablero[i+1][j]==tablero[i+2][j]==tablero[i+3][j]=="O")):
                return False
            else:
                return True
def revisar_filas(tablero,filas,columnas):
    for i in range (0,filas):
        for j in range (0,columnas-3):
            if ((tablero[i][j]==tablero[i][j+1]==tablero[i][j+2]==tablero[i][j+3]=="X") or (tablero[i][j]==tablero[i][j+1]==tablero[i][j+2]==tablero[i][j+3]=="O")):
                return False
            else:
                return True
def revisar_diagonal_derecha(tablero,filas,columnas):
    for j in range (0,columnas-3):
        for i in range (filas-3,filas):
            if ((tablero[i][j]==tablero[i-1][j+1]==tablero[i-2][j+2]==tablero[i-3][j+3]=="X") or (tablero[i][j]==tablero[i-1][j+1]==tablero[i-2][j+2]==tablero[i-3][j+3]=="O")):
                return False
            else:
                return True
def revisar_diagonal_izquierda(tablero,filas,columnas):
    for j in range (0,columnas-3):
        for i in range (0,filas-3):
            if ((tablero[i][j]==tablero[i+1][j+1]==tablero[i+2][j+2]==tablero[i+3][j+3]=="X") or (tablero[i][j]==tablero[i+1][j+1]==tablero[i+2][j+2]==tablero[i+3][j+3]=="O")):
                return False
            else:
                return True
def comprobar_ganador(tablero,filas,columnas):
    resultado=revisar_columnas(tablero,filas,columnas) or revisar_filas(tablero,filas,columnas) or revisar_diagonal_derecha(tablero,filas,columnas) or revisar_diagonal_izquierda(tablero,filas,columnas)
juego=True
while juego==True:
    table=introducir_ficha(table,f,c)
    ver_tablero(table)
    juego=comprobar_ganador(table,f,c)
#SOL DEL PROFE
