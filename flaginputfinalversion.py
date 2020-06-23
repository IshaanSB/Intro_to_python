import turtle

def swiss_flag():
    t = turtle.Turtle()
    t.color('red')
    t.begin_fill()
    t.pencolor('red')
    t.lt(180)
    t.fd(300)
    t.rt(90)
    t.fd(350)
    t.rt(90)
    t.fd(650)
    t.rt(90)
    t.fd(350)
    t.rt(90)
    t.fd(350)
    t.end_fill()
    t.up()
    t.color('white')
    t.pencolor('white')
    t.rt(90)
    t.fd(70)
    print(t.pos())
    t.down()
    t.begin_fill()
    t.fd(250)
    t.rt(90)
    t.fd(75)
    t.rt(90)
    t.fd(250)
    t.rt(90)
    t.fd(75)
    t.up()
    t.rt(90)
    t.fd(100)
    t.lt(90)
    t.down()
    t.fd(100)
    t.rt(90)
    t.fd(65)
    t.rt(90)
    t.fd(275)
    t.rt(90)
    t.fd(65)
    t.rt(90)
    t.fd(175)
    t.end_fill()









def banglad_flag():
    t = turtle.Turtle()
    t.color('green')
    t.begin_fill()
    t.pencolor('green')
    t.lt(180)
    t.fd(300)
    t.rt(90)
    t.fd(350)
    t.rt(90)
    t.fd(650)
    t.rt(90)
    t.fd(350)
    t.rt(90)
    t.fd(350)
    t.end_fill()
    t.up()
    t.color('red')
    t.pencolor('red')
    t.rt(90)
    t.setpos(125,175)
    t.down()
    t.begin_fill()
    t.hideturtle()
    t.circle(100)
    t.end_fill()



   














def Indian_flag():
    t = turtle.Turtle()
    t.color("orange")
    t.begin_fill()
    t.pencolor('orange')
    t.lt(180)
    t.fd(300)
    t.rt(90)
    t.fd(100)
    t.rt(90)
    t.fd(450)
    t.rt(90)
    t.fd(100)
    t.rt(90)
    t.fd(150)
    t.end_fill()
    t.penup()
    t.fd(300)
    t.lt(90)
    t.pendown()
    t.color("black")
    t.pencolor("black")
    t.fd(100)
    t.lt(90)
    t.fd(450)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(450)
    t.penup()
    t.lt(90)
    t.fd(100)
    t.color("green")
    t.begin_fill()
    t.pencolor("green")
    t.pendown()
    t.fd(100)
    t.lt(90)
    t.fd(450)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(450)
    t.end_fill()
    t.penup()
    t.rt(90)
    t.fd(100)
    t.rt(90)
    t.fd(225)
    t.color("blue")
    t.pencolor("blue")
    t.rt(90)
    t.fd(30)
    t.penup()
    t.setpos(-105,-50)
    t.pendown()
    t.circle(45)
    t.lt(90)
    t.penup()
    t.fd(50)
    t.penup()
    t.setpos(-60,-90)
    t.pendown()
    t.color("blue")
    t.begin_fill()
    t.circle(40)
    t.hideturtle()
    t.end_fill()










def Czech_republic():
    t = turtle.Turtle()
    #turtle.textinput("CF","Where are you from?")
    t.lt(180)
    t.fd(300)
    t.rt(90)
    t.fd(350)
    t.rt(90)
    t.fd(650)
    t.rt(90)
    t.fd(350)
    t.rt(90)
    t.fd(350)
    t.up()
    t.fd(300)
    t.color('blue')
    t.pencolor('blue')
    t.rt(150)
    t.down()
    t.begin_fill()
    t.fd(350)
    t.lt(120)
    t.fd(350)
    t.end_fill()
    t.up()
    t.color('red')
    t.pencolor('red')
    t.rt(150)
    t.fd(650)
    t.rt(90)
    t.fd(175)
    t.rt(90)
    t.color('black')
    t.pencolor('black')
    t.down()
    t.color('red')
    t.begin_fill()
    t.fd(350)
    t.lt(125)
    t.rt(95)
    t.fd(350)
    t.lt(150)
    t.up()
    t.fd(650)
    t.lt(90)
    t.fd(175)
    t.down()
    t.end_fill()
    t.down()
    t.pensize(width=5)
    t.bk(175)
    





country_flag = turtle.textinput("CF","Where are you from?")

if country_flag.lower == "czech":
    Czech_republic()
    
   
#if country_flag == "india":
        #Indian_flag()
        


elif country_flag.lower == "india":
    Indian_flag()
    
elif country_flag.lower == "bangladesh":
    banglad_flag()
    
elif country_flag.lower == "switzerland":
    swiss_flag()
    
else:
    print("Sorry But Your Country\'s flag has not been implemented yet, Expect more awesome additions!!")
    

    
 

        
        


 


       
    
        
        
        

    
    
    
    
    
   
   
    

    
    






    

'''t = turtle.Turtle()
my_country = "czech"
my_flag = str(country_flag)
if (my_flag == my_country):
    print("czech")
'''

'''Czech_republic()
'''
    
    

    
