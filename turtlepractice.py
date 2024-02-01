import turtle

window = turtle.Screen()
pen=turtle.Turtle()
try:
    shape=(input("3,4,or 5 sides?: "))


    if shape==("3"):
        pen.fillcolor('green')
        pen.begin_fill()
        pen.forward(100) 
        pen.right(-120) 

        pen.forward(100) 
        pen.right(-120) 

        pen.forward(100) 
        pen.right(-120) 
        pen.end_fill()

        turtle.exitonclick()
    elif shape==("4"):
        pen.fillcolor('blue')
        pen.begin_fill()

        pen.forward(100)
        pen.left(90)

        pen.forward(100)
        pen.left(90)

        pen.forward(100)
        pen.left(90)

        pen.forward(100)
        pen.end_fill()

        turtle.exitonclick()
    elif shape==("5"):
        pen.fillcolor('red')
        pen.begin_fill()

        pen.forward(100)
        pen.left(72)
        
        pen.forward(100)
        pen.left(72)

        pen.forward(100)
        pen.left(72)

        pen.forward(100)
        pen.left(72)

        pen.forward(100)
        pen.end_fill()
        turtle.exitonclick()
    else:
        print("error:  enter 3, 4, or 5.")
    

except: print("error- simple code- how did you manage to break it??")
    
