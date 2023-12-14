# import turtle
import turtle
import random

ninja = turtle.Turtle()

ninja.speed(10)


  
# colormode should be 255 to 
# show every type of color
turtle.colormode(255)

for i in range(random.randint(60,101)):
    val = random.randint(1,8)
    # size of the pen
    ninja.pensize(val)
    ninja.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))                  
    ninja.forward(100)
    ninja.right(val * i)
    ninja.forward(val * i)
    ninja.left(val * i)
    ninja.forward(val + 50)
    ninja.right(val * i)
    
    ninja.penup()
    ninja.setposition(val * 5, val + 80)
    ninja.pendown()
    
    ninja.right(2 * i)
    
turtle.done()



