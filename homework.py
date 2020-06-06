'''write a python program to ask the name and hobby of 6 people. 
put name and hobby as key, value pair in dictionary.
'''
name = input("What is your name?")
print("Hi there!" , name )
hobby = input("What is your hobby?")
print("Nice to know!" , name )

activities = {name : hobby}

print(activities)


