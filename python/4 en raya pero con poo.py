#PROFE
class CuatroEnRaya:
    def __init__(self, filas, columnas):
        self.filas=filas
        self.columnas=columnas
        self.tablero=self.crear_tablero()
        self.turno=None
    def crear_tablero(self):
        tablero=[None]*self.filas
        for f in range(self.filas):
            tablero[f]=["."]*self.columnas
        return tablero
    def mostrar_tablero(self):
        for num in range(self.columnas):
            print(f"{num}", end="  ")
        for i in self.tablero:
            print("")
            for j in i:
                print(f"{j}", end="  ")
    def introducir_ficha(self,c,color):
        if c >= self.columnas or c < 0:
            print("Error. Fuera de Rango...")
            return
        elif self.tablero[0][c] != '.':
            print("Columna llena de Fichas...")
        else:
            for fila in range (self.filas-1,-1,-1):
                if self.tablero[fila][c] == '.':
                    self.tablero[fila][c]=color
                    return
    def revisar_filas(self, color):
        for r in range (self.filas):
            for c in range (self.columnas-3):
                if self.tablero[r][c] == color and self.tablero[r][c+1] == color and self.tablero[r][c+2] == color and self.tablero[r][c+3] == color:
                    return True
    def revisar_columnas(self, color):
        for c in range (self.columnas):
            for r in range (self.filas-3):
                if self.tablero[r][c] == color and self.tablero[r+1][c] == color and self.tablero[r+2][c] == color and self.tablero[r+3][c] == color:
                    return True
    def revisar_diagonal_derecha(self, color):
        for c in range (self.columnas-3):
            for r in range (self.filas-1,2,-1):
                if self.tablero[r][c] == color and self.tablero[r-1][c+1] == color and self.tablero[r-2][c+2] == color and self.tablero[r-3][c+3] == color:
                    return True
    def revisar_diagonal_izquierda(self, color):
        for c in range (self.columnas-1,2,-1):
            for r in range (self.filas-1,2,-1):
                if self.tablero[r][c] == color and self.tablero[r-1][c-1] == color and self.tablero[r-2][c-2] == color and self.tablero[r-3][c-3] == color:
                    return True
    def comprobar_ganador(self, color):
        return self.revisar_filas(color) or self.revisar_columnas(color) or self.revisar_diagonal_derecha(color) or self.revisar_diagonal_izquierda(color)
    def jugar(self, player1='X', player2='O'):
        self.turno=player2
        while True:
            if self.turno==player2:
                self.turno=player1
            else:
                self.turno=player2
            self.mostrar_tablero()
            columna=int(input(f"Turno del jugador {self.turno}: "))
            self.introducir_ficha(columna, self.turno)
            if self.comprobar_ganador(self.turno):
                print(f"Gana el jugador: {self.turno}")
                self.mostrar_tablero()
                break
juego=CuatroEnRaya(6,7)
juego.jugar()
#JONNY
class Juego:
    def __init__(self, filas, columnas):
        self.filas=filas
        self.columnas=columnas
        self.turno="X"
        self.sig_turno="O"
    def crear_tabla(self):
        tablero=[None]*self.filas
        for i in range (self.filas):
            tablero[i]=["."]*self.columnas
        return tablero
    def mostrar_tablero(self, tablero):
        for num in range(self.columnas):
            print(f"{num}", end="  ")
        for i in tablero:
            print("")
            for j in i:
                print(f"{j}", end="  ")
    def introducir_ficha(self,tablero,c,color):
        if c >= self.columnas or c < 0:
            print("Error. Fuera de Rango...")
            return
        elif tablero[0][c] != '.':
            print("Columna llena de Fichas...")
        else:
            for fila in range (len(tablero)-1,-1,-1):
                if tablero[fila][c] == '.':
                    tablero[fila][c]=color
                    return tablero
    def revisar_filas(self,tablero,color):
        for r in range (self.filas):
            for c in range (self.columnas-3):
                if tablero[r][c] == color and tablero[r][c+1] == color and tablero[r][c+2] == color and tablero[r][c+3] == color:
                    return True
    def revisar_columnas(self,tablero,color):
        for c in range (self.columnas):
            for r in range (self.filas-3):
                if tablero[r][c] == color and tablero[r+1][c] == color and tablero[r+2][c] == color and tablero[r+3][c] == color:
                    return True
    def revisar_diagonal_derecha(self,tablero,color):
        for c in range (self.columnas-3):
            for r in range (self.filas-1,2,-1):
                if tablero[r][c] == color and tablero[r-1][c+1] == color and tablero[r-2][c+2] == color and tablero[r-3][c+3] == color:
                    return True
    def revisar_diagonal_izquierda(self,tablero,color):
        for c in range (self.columnas-1,2,-1):
            for r in range (self.filas-1,2,-1):
                if tablero[r][c] == color and tablero[r-1][c-1] == color and tablero[r-2][c-2] == color and tablero[r-3][c-3] == color:
                    return True
    def comprobar_ganador(self,tablero,color):
        return Juego.revisar_filas(tablero,color) or Juego.revisar_columnas(tablero,color) or Juego.revisar_diagonal_derecha(tablero,color) or Juego.revisar_diagonal_izquierda(tablero,color)
    def iniciar_juego(self,tablero):
        while True:
            self.turno=self.sig_turno
            Juego.mostrar_tablero(self,tablero)
            if self.turno == 'X':
                columna=int(input("Turno de X: "))
                self.sig_turno='O'
            elif self.turno == 'O':
                columna=int(input("Turno de O: "))
                self.sig_turno='X'
            Juego.introducir_ficha(self,tablero,columna, self.turno)
            if Juego.comprobar_ganador(self,tablero,self.turno):
                print(f"Ganador el jugador: {self.turno}\n")
                Juego.mostrar_tablero(tablero)
                break
enraya=Juego(6,7)
table=enraya.crear_tabla()
#enraya.mostrar_tablero(table)
enraya.iniciar_juego(table)