'''If you were standing on the moon right now, your weight would be

16.5 percent of what it is on Earth. You can calculate that by multiplying

your Earth weight by 0.165.

If you gained a kilo in weight every year for the next 15 years,

what would your weight be when you visited the moon each year

and at the end of the 15 years? Write a program using a for loop

that prints your moon weight for each year.
'''
Earth_weight = int(input('What is your weight?'))
MWTY = Earth_weight * 0.165
for y in range(0,16):
    MWTY = MWTY + 0.165
    
    print(MWTY)
    
    
    
    
    
    

    
    
   
    
    
   
    
    
    
    