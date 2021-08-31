
import turtle

def draw_square(t, input_angle):
    degree = 90 + input_angle
    t.fillcolor('orange')
    t.begin_fill()
    #t.fd(100)
    t.left(degree)
    t.fd(100)
    t.left(90)
    t.fd(100)
    t.left(90)
    t.fd(100)
    t.left(90)
    t.fd(100)
    t.end_fill()

s = turtle.getscreen()
t = turtle.Turtle()
t.speed(1)

for angle in range(0,5):
    draw_square(t, 15 * angle)
turtle.exitonclick()



