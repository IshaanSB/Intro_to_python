#Write python program to convert decimal number to binary.

#first write the steps and then write the program on a notebook

#make a dict that contains and converts decimals - binaries
conversion_dict = {'0' : '0000' , '1' : '0001' , '2' : '0010' , '3' : '0011' , '4' : '00100' , '5' : '00101' , '6' : '00110' , '7' : '00111' , '8' : '01000' , '9' : '01001'	, '10' : '01010' , '.' : '-'}


#ask for user input and store it in a variable
decimal_input = input('Enter a decimal number:')

for y in decimal_input:
    if y in conversion_dict:
        print(conversion_dict[y] ,end = "")
    