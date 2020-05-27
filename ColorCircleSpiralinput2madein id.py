import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
colors = ["red", "yellow", "blue", "green" ,
          "gray" , "purple" ,  "white" , "Crimson"]
          
sides = int(turtle.numinput("Number of sides" ,
                                           "How many sides do you want between (1-8)?" , 4 , 1 , 8))
                            
for x in range(360):
    t.pencolor( colors[ x % sides] )
    t.circle(x)
    t.left(95)
    
    t.left(360 / sides + 1)
    t.width(x * sides / 200)
    
 
    



