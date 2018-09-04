import turtle
from turtle import*
donatello = turtle.Turtle()
win = turtle.Screen()
win.bgcolor('white')
donatello.pencolor('red')
donatello.speed(1)

repCount = 0

while repCount < 4:
    donatello.forward(150)
    donatello.left(90)
    repCount = repCount + 1
