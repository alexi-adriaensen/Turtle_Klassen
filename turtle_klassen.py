import turtle
import random


scherm = turtle.Screen()
pen = turtle.Turtle()
pen.speed(0)
class Square:
    def __init__(self, xcord, ycord, size):
        self.xcord = xcord
        self.ycord = ycord
        self.size = size

    def teken(self):
        pen.penup()
        pen.goto(self.xcord, self.ycord)
        pen.pendown()
        for _ in range(4):
            pen.forward(self.size)
            pen.left(90)

for _ in range(1000):
    x = random.randint(-500, 500)
    y = random.randint(-200, 200)
    size = random.randint(20, 80)
    square = Square(x, y, size)
    square.teken()

turtle.exitonclick()
