#averageofnums
import sys
'''def avg(list_b):
    for x in range(2,10):
        for i in list_b:
            if x > 10:
                break
            elif x < 10:
               y = len(list_b)
            for x in list_b:
                for n in range(0,y):
                   Sum = sum(list_b)
                   return Sum / y
'''                
def average(list_a):
   y = len(list_a)
   Sum3 = 0
   if y > 10:
       print("Error numbers in the list should be lower than 10")
       sys.exit()
       
   
   for x in list_a:
       Sum3 = Sum3 + x
    
   return Sum3 / y
       
       
                   
                
           
            
            
            
r = [5,5,5,8]

print(average(r))
        
        
        
            
    
    
    