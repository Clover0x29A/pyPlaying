import random
import turtle

this_array = []

def create_array(row, col):
    new_array = []
    for x in range(row):
        new_array.append([])
        for y in range(col):
            if x == 0 or x == row - 1:
                new_array[x].append(1)
            elif y == 0 or y == col - 1:
                new_array[x].append(1)
            else:
                new_array[x].append(0 if random.random() < 0.666 else 1)
    return new_array

def draw_map(map, t, start_x, start_y):
    for x in range(len(map[0])):
        t.penup()
        t.goto(start_x, start_y - x * 15)
        t.pendown()
        for y in range(len(this_array[x])):
            if this_array[x][y] == 1:
                t.dot(15)
                t.penup()
                t.fd(15)
                t.pendown()
            else:
                t.penup()
                t.fd(15)
                t.pendown()
        
        


row = 20
col = 20

this_array = create_array(row, col)
#print(this_array)

start_x = 0 - row * 10
start_y = 0 + col * 10
screen = turtle.getscreen()
t = turtle.Turtle()
t.hideturtle()
t.clear()
t.speed(150)
t.penup()
t.goto(start_x, start_y)
draw_map(this_array, t, start_x, start_y)


turtle.exitonclick()

#for x in range(len(this_array)):
#    print(this_array[x])