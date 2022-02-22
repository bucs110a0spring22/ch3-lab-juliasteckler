import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. your code goes here
x = random.randrange(1, 100)
y = random.randrange(1, 100)
leonardo.forward(x)
michelangelo.forward(y)
leonardo.goto(-100,-20)
michelangelo.goto(-100,20)
for i in range(10):
  a = random.randrange(0, 10)
  b = random.randrange(0, 10)
  for i in range(10):
    leonardo.forward(a)
    michelangelo.forward(b)
leonardo.goto(-100,-20)
michelangelo.goto(-100,20)
# Part B - complete part B here
leonardo.down()
for i in range(3):
  leonardo.forward(30)
  leonardo.right(360/3)
leonardo.clear()
for i in range(4):
  leonardo.forward(30)
  leonardo.right(360/4)
leonardo.clear()
for i in range(6):
  leonardo.forward(20)
  leonardo.right(360/6)
leonardo.clear()
for i in range(9):
  leonardo.forward(20)
  leonardo.right(360/9)
leonardo.clear()
for i in range(12):
  leonardo.forward(20)
  leonardo.right(360/12)
leonardo.clear()
leonardo.up()
window.exitonclick()