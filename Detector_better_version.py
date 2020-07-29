#dict that contains element symbols
symbols_dict = {'H' : '1' , 'He' : '2' , 'Li' : '3' , 'Be' :'4' , 'B' : '5' , 'C' : '6' , 'N' : '7' , 'O' : '8'}

print(symbols_dict)

symbol_input = input('Choose one of the elements form the dict:')

atomic_mass_dict = {'H' : '1' , 'He' : '4' , 'Li' : '7' , 'Be' : '9' , 'B' : '11' , 'C' : '12' , 'N' : '14' , 'O' : '16'}

names_of_element_dict = {'H' : 'Hydrogen' , 'He' : 'Helium' , 'Li' : 'Lithium' , 'Be' : 'Beryllium' , 'B' : 'Boron' , 'C' : 'Carbon' , 'N' : 'Nitrogen' , 'O' : 'Oxygen'}

input_symbol = symbol_input

for y in symbols_dict:
    if symbol_input == y:
        print('atomic number is:-')
        print(symbols_dict[y])
        break

else:
    for x in symbol_input:
        if x in symbols_dict:
            print(symbols_dict[x])
            break
           
for a in atomic_mass_dict:
    if a == symbol_input:
        print('atomic mass is:-')
        print(atomic_mass_dict[a])

print('element\'s name is:-')




for r in names_of_element_dict:
    if symbol_input == r:
        print(names_of_element_dict[r])
        break
    else:
        for b in symbol_input:
            if b in names_of_element_dict:
                break
                print(names_of_element_dict[b])
                


   
    
