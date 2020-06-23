#1) write a program to get factors of given number. 
#2) write a program to write table of 1 to 10.

user_input = int(input('Enter a Number:'))

for x in range(1,user_input + 1):
    if user_input % x == 0:
        print(x)
        
        
        
