# palindromecheck

#ask the user for a string
string_input = input('Enter any string:')
 #store it in a list over what we iterated and produce a word
new_list = []
# go over each letter in a string
for x in string_input:
   
    # adds the letters to the list
    new_list.append(x)
print(new_list)

list_2 = []
# required to iterate over the string the user gave backwards
l = len(string_input)
#where it should it end
for n in range(0,l):
    #to assign the letter in the list to form the word (for comparison)
    new_list[n]


   






for y in range(l -1 ,-1,-1):
    # adds the letters to the list
    list_2.append(new_list[y])
    
for x in range(0,l):
    #to assign the letter in the list to form the word (for comparison)
      list_2[x]
    


  

# to check whether it is a palindrome or not
if list_2 == new_list:
    print("the word is a palindrome")
else:
    print("word is not a palindorme")
    
    
    
 
    
        
       
        
    
    

    
    
    

        
    
   
    
    