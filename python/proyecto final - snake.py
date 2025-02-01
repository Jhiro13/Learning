import turtle
import time
import random
class SnakeGame:
    def __init__(self):
    #----Ventana----
        self.ventana=turtle.Screen()
        self.ventana.bgcolor("green")
        self.ventana.title("Juego Snake")
        self.ventana.setup(600,600)
        self.ventana.tracer(0)
    #----Serpiente----
        self.snake=turtle.Turtle()
        self.snake.speed(0)
        self.snake.shape("square")
        self.snake.color("black")
        self.snake.penup()
    #----comida----
        self.comida=turtle.Turtle()
        self.comida.speed(0)
        self.comida.shape("circle")
        self.comida.color("red")
        self.comida.penup()
        self.comida.setx((random.random()-0.5)*520)
        self.comida.sety((random.random()-0.5)*520)
    #----Score----
        self.puntuacion=0
        self.record=0
        self.cuerpo=[]
        self.score=turtle.Turtle()
        self.score.color("white")
        self.score.penup()
        self.score.hideturtle()
        self.score.goto(0,250)
        self.print_score()
    #----Para asignar movimientos a las teclas
        self.ventana.listen()
        self.ventana.onkeypress(self.arriba,"w")
        self.ventana.onkeypress(self.abajo,"s")
        self.ventana.onkeypress(self.derecha,"d")
        self.ventana.onkeypress(self.izquierda,"a")
    #----Movimientos de la serpiente----
        self.direccion=None
        self.delay=0.1
    def arriba(self):
        if self.direccion!="abajo":
            self.direccion="arriba"
    def abajo(self):
        if self.direccion!="arriba":
            self.direccion="abajo"
    def derecha(self):
        if self.direccion!="izquierda":
            self.direccion="derecha"
    def izquierda(self):
        if self.direccion!="derecha":
            self.direccion="izquierda"
    def move(self):
        hx,hy=self.snake.xcor(), self.snake.ycor()
        for i in range(len(self.cuerpo)-1,0,-1):
            x=self.cuerpo[i-1].xcor()
            y=self.cuerpo[i-1].ycor()
            self.cuerpo[i].goto(x,y)
        if len(self.cuerpo)>0:
            self.cuerpo[0].goto(hx,hy)
        if self.direccion=="arriba":
            self.snake.sety(hy+20)
        elif self.direccion=="abajo":
            self.snake.sety(hy-20)
        elif self.direccion=="izquierda":
            self.snake.setx(hx-20)
        elif self.direccion=="derecha":
            self.snake.setx(hx+20)
    def jugar(self): 
        while True:
            self.ventana.update()
            self.colision()
            self.comer()
            self.colision_cuerpo()
            time.sleep(self.delay)
            self.move()   
        self.ventana.mainloop()
    def colision(self):
        if self.snake.ycor()>270 or self.snake.ycor()<-270 or self.snake.xcor()<-270 or self.snake.xcor()>270:
            self.reset()
    def colision_cuerpo(self):
        for s in self.cuerpo:
            if s.distance(self.snake)<20:
                self.reset()
    def comer(self):
        if self.snake.distance(self.comida)<20:
            x=(random.random()-0.5)*520
            y=(random.random()-0.5)*520
            self.comida.setx(x)
            self.comida.sety(y)
            self.incrementar_cuerpo()
            self.puntuacion+=10
            self.print_score()
    def incrementar_cuerpo(self):
        segmento=turtle.Turtle()
        segmento.speed(0)
        segmento.shape("square")
        segmento.color("blue")
        segmento.penup()
        self.cuerpo.append(segmento)
    def reset(self):
        time.sleep(1)
        self.snake.goto(0,0)
        self.direccion=None
        if self.puntuacion>self.record:
            self.record=self.puntuacion
        self.puntuacion=0
        for s in self.cuerpo:
            s.hideturtle()
        self.cuerpo.clear()
        self.print_score()
    def print_score(self):
        self.score.clear()
        self.score.write(f"Puntuación: {self.puntuacion}        Record: {self.record}", align="center", font=("Arial", 16, "bold"))
juego=SnakeGame()
juego.jugar()
