import turtle
import random

screen = turtle.Screen()
screen.bgcolor(0,0,0)
screen.title("Roses")
spot = turtle.Turtle() #my very first pet was a tortoise named Spot, hence the name
spot.color("black")

# while True:
#     spot.right(random.randint(0,360))
#     spot.forward(random.randint(90,200))

#     pos = spot.position()

#     if pos[0] < 0:
#         spot.goto(400,pos[1])
#     elif pos[0] > 400:
#         spot.goto(0,pos[1])
#     elif pos[1] < 0:
#         spot.goto(pos[0], 300)
#     elif pos[1] > 300:
#         spot.goto(pos[0], 0)


t = turtle.Pen()
turtle.bgcolor('black')
t.pencolor("red")
for i in range(12):
    for x in range(60):
        t.width(x//100 + 1)
        t.forward(x)
        t.left(59)
    t.up()
    t.goto(random.randint(50,350), random.randint(50,250))
    t.down()


turtle.exitonclick
