
import turtle

def draw_square(t, input_angle, angle):
    degree = 90 + input_angle
    if angle == 0:
        angle = 1
    my_red = angle * input_angle + 40
    my_green = (my_red % 2) * 2
    my_blue = my_red % angle
    if my_red > 255:
        my_red = 244
    if my_green > 255:
        my_green = 255
    if my_blue < 0:
        my_blue = 155
    t.color((my_red,my_green, my_blue))
    t.begin_fill()
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
s.colormode(255)
t = turtle.Turtle()
t.speed(5)

for angle in range(0,19):
    draw_square(t, 15, angle)
turtle.exitonclick()



