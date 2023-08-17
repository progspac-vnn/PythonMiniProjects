import turtle
import random
win = turtle.Screen()
win.setup(width=500, height= 500)
win.bgcolor('black')
win.title('Dice')
win.tracer(0)

def click():
    num = random.randint(1,6)
    print(num)
    print('clicked')
    if num == 1:
        # 0
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('red')
        dot.penup()
        dot.goto(0,0)

        # 1
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('black')
        dot.penup()
        dot.goto(-125,125)

         # 2
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('black')
        dot.penup()
        dot.goto(-125,0)

        # 3
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('black')
        dot.penup()
        dot.goto(-125,-125)
        
         # 4
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('black')
        dot.penup()
        dot.goto(125,125)

        # 5
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('black')
        dot.penup()
        dot.goto(125,0)
        
         # 6
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('black')
        dot.penup()
        dot.goto(125,-125)
    if num == 2:
        # 0
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('black')
        dot.penup()
        dot.goto(0,0)

        # 1
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('red')
        dot.penup()
        dot.goto(-125,125)

         # 2
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('black')
        dot.penup()
        dot.goto(-125,0)

        # 3
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('black')
        dot.penup()
        dot.goto(-125,-125)
        
         # 4
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('black')
        dot.penup()
        dot.goto(125,125)

        # 5
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('black')
        dot.penup()
        dot.goto(125,0)
        
         # 6
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('red')
        dot.penup()
        dot.goto(125,-125)
    if num == 3:
        # 0
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('red')
        dot.penup()
        dot.goto(0,0)

        # 1
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('red')
        dot.penup()
        dot.goto(-125,125)

         # 2
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('black')
        dot.penup()
        dot.goto(-125,0)

        # 3
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('black')
        dot.penup()
        dot.goto(-125,-125)
        
         # 4
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('black')
        dot.penup()
        dot.goto(125,125)

        # 5
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('black')
        dot.penup()
        dot.goto(125,0)
        
         # 6
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('red')
        dot.penup()
        dot.goto(125,-125)

    if num ==4:
        # 0
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('black')
        dot.penup()
        dot.goto(0,0)

        # 1
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('red')
        dot.penup()
        dot.goto(-125,125)

         # 2
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('black')
        dot.penup()
        dot.goto(-125,0)

        # 3
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('red')
        dot.penup()
        dot.goto(-125,-125)
        
         # 4
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('red')
        dot.penup()
        dot.goto(125,125)

        # 5
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('black')
        dot.penup()
        dot.goto(125,0)
        
         # 6
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('red')
        dot.penup()
        dot.goto(125,-125)
    if num == 5:
        # 0
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('red')
        dot.penup()
        dot.goto(0,0)

        # 1
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('red')
        dot.penup()
        dot.goto(-125,125)

        # 2
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('black')
        dot.penup()
        dot.goto(-125,0)

        # 3
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('red')
        dot.penup()
        dot.goto(-125,-125)
        
        # 4
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('red')
        dot.penup()
        dot.goto(125,125)

        # 5
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('black')
        dot.penup()
        dot.goto(125,0)
        
        # 6
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('red')
        dot.penup()
        dot.goto(125,-125)
    if num == 6:
        # 0
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('black')
        dot.penup()
        dot.goto(0,0)

        # 1
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('red')
        dot.penup()
        dot.goto(-125,125)

        # 2
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('red')
        dot.penup()
        dot.goto(-125,0)

        # 3
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('red')
        dot.penup()
        dot.goto(-125,-125)
        
        # 4
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('red')
        dot.penup()
        dot.goto(125,125)

        # 5
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('red')
        dot.penup()
        dot.goto(125,0)
        
        # 6
        dot = turtle.Turtle()
        dot.shape('circle')
        dot.color('red')
        dot.penup()
        dot.goto(125,-125)



# key
win.listen()
win.onkeypress(click, 'Up')


while True:
    win.update()


win.mainloop()