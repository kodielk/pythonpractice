import turtle

t = turtle.Turtle()



def main():
    def triangleS(length, scaleFactor):
        '''draws a triangle to whatever size you want.'''
        for _ in range(3):
            t.forward(length * scaleFactor)
            t.left(120)

    def rectangle(length, tallness, scaleFactor):
        '''draws a rectangle to whatever size you want.'''
        for _ in range(2):
            t.forward(length * scaleFactor)
            t.left(90)
            t.forward(tallness * scaleFactor)
            t.left(90)

    def circleS(size):
        '''draws a circle of whatever size you want.'''
        t.circle(size)

    #circle tree
    t.penup()
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.pendown()
    t.color("darkgreen")
    t.begin_fill()
    circleS(30)
    t.end_fill()
    #2nd circle
    t.penup()
    t.forward(75)
    t.left(90)
    t.forward(85)
    t.pendown()
    t.color("darkgreen")
    t.begin_fill()
    circleS(60)
    t.end_fill()
    t.penup()
    t.forward(80)
    t.pendown()
    #3rd circle
    t.color("darkgreen")
    t.begin_fill()
    circleS(40)
    t.end_fill()
    t.penup()
    t.goto(200,100)
    t.forward(80)
    t.pendown()
    #trunk
    t.fillcolor("chocolate4")
    t.begin_fill()
    rectangle(5,200,1)
    t.end_fill()
    #scootin and drawing next tree
    t.penup()
    t.goto(-300,0)
    t.pendown()
    t.left(180)
    t.fillcolor("darkolivegreen")
    t.begin_fill()
    triangleS(100,1.5)
    t.forward(75)
    t.right(180)
    t.end_fill()
    t.fillcolor("chocolate4")
    t.begin_fill()
    rectangle(5,200,1)
    t.end_fill()
    t.right(290)
    #hammock...sigh...
    t.color("blue4")
    t.begin_fill()
    #hammock strap
    rectangle(5,100,1)
    #hammock top, and other strap
    t.left(90)
    t.forward(100)
    t.left(20)
    t.forward(150)
    t.left(20)
    t.forward(100)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(10)
    t.right(180)
    t.forward(10)
    t.right(50)
    t.forward(30)
    t.right(50)
    t.forward(75)
    t.right(25)
    t.forward(50)
    t.right(50)
    t.forward(50)
    t.end_fill()


if __name__ == "__main__":
    main()
    turtle.mainloop()
