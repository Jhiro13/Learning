import turtle

def draw_circle(color, x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_rectangle(color, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_spiderman():
    turtle.speed(3)
    
    # Cabeza
    draw_circle("red", 0, 50, 50)

    # Ojos
    draw_rectangle("white", -20, 70, 20, 30)
    draw_rectangle("white", 10, 70, 20, 30)

    # Cuerpo
    draw_rectangle("blue", -20, 0, 40, 60)

    # Brazos
    draw_rectangle("red", -50, 20, 30, 10)
    draw_rectangle("red", 20, 20, 30, 10)

    # Piernas
    draw_rectangle("red", -20, -40, 10, 30)
    draw_rectangle("red", 10, -40, 10, 30)

    # Telaraña
    turtle.penup()
    turtle.goto(0, 50)
    turtle.pendown()
    turtle.color("black")
    turtle.goto(0, 100)

    # Finalizar dibujo
    turtle.hideturtle()
    turtle.done()

draw_spiderman()