import turtle
import random
screen=turtle.Screen()
screen.bgcolor("white")
my_turtle=turtle.Turtle()
my_turtle.speed(0)
colors=["red","orange","yellow","green","blue","indigo","violet"]
for i in range(100):
	my_turtle.color(random.choice(colors))
	my_turtle.circle(50)
	my_turtle.forward(10)
	my_turtle.right(10)
turtle.done()
