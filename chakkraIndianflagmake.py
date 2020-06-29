import turtle

t = turtle.Turtle()

t.color('blue')
t.pensize(5)

t.circle(50)
t.up()
print(t.setpos(0,35))
t.pensize(0)
t.down()
t.begin_fill()
t.circle(15)
t.end_fill()


for x in range(1,25):
    t.color('red')
    t.up()
    t.rt(85+20)
    t.color('blue')
    t.down()
    t.pensize(0)
    
    
    t.setpos(0,47)
    t.fd(35+15)
    t.color('red')
    t.up()
    t.hideturtle()
    #while i :
    #t.setpos(0,30)
    
        
     
    
    
   
    #t.setpos(0,30)
    


   

'''
t.rt(25)
t.color('blue')
t.down()
t.fd(40)
t.color('red')
t.up()
t.setpos(0,40)


t.rt(25)
t.color('blue')
t.down()
t.fd(40)
t.color('red')
t.up()
t.setpos(0,40)


t.rt(y)
'''













'''t.color('red')
t.up()
t.rt(85)
t.color('blue')
t.down()
t.pensize(5)
t.fd(35)
t.color('red')
t.up()
t.bk(35)

t.rt(25)
t.color('blue')
t.down()
t.fd(35)
t.color('red')
t.up()
t.bk(35)

'''

