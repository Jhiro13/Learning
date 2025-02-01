import turtle as t
#SE CONSIDERA A UNA PANTALLA COMO UNA CLASE
#Y A LA TORTUGA TAMBIEN COMO UNA CLASE
pantalla=t.Screen()
pantalla.title("QUE ONDA PLEBES")#es para establecer el título de la pantalla
pantalla.bgcolor("orange")#es para el color de fondo
pantalla.setup(0.8,0.8)#para configurar las dimensiones de la pantalla
pantalla.tracer(1,25)#para activar o desactivar la animación/el primero no sé para que es y el segundo es para el delay del dibujo
def a():
    t.fd(50)
pantalla.onkeypress(a,"Up")#ejecuta el metodo al presionar la tecla up
pantalla.listen()#esta nota te recolecta eventos clave nms
tortuga=t.Turtle()#crea y configuras a la tortuga
tortuga.shape("turtle")#le indicas la forma predeterminada que tenga la tortuga
tortuga.color("green")#color de la tortuga
#pendown() y penup() indican cuando levantar o apoyar durante el movimiento de la tortuga
tortuga.pensize(2)
tortuga.speed(4)#te permite modificar la velocidad de la tortuga, solo del 1 al 10
tortuga.circle(50)
tortuga.goto(21,19)#goto()/setpos()/setposition() -> te mueve a una cordenada dibujando una linea
tortuga.write("QLQ MMGUEVO")#escribe en la posición actual
tortuga.hideturtle()#te esconde a la tortuga
pantalla.mainloop()#para que la pantalla quede abierta