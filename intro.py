print("Hello World from Python!")
print(2)
print(5+3)
#Boolean must always have first letter Caps
print(True)
# Single line comment
""" 
Multi-line comment

"""

#Variable creation
name = "Jeuan"
age = 54
middle_name = "Montez"
last_name = "Mitchell"
found = False
print(name)
print(age)
print(name, age)

#Can't concotanate string and number, turn number/boolean to string using str(variable)
print("My name is " + name + ", and I am " + str(age) + ".")

print("Did he show up to class?" + str(found))
print(name, middle_name, last_name, age)

#addName = Js Camel Case
#add_name = Py Snake Case
#Tells you what type the var is
print(type(name))
print(type(age))
print(type(found))

#Casting helps us convert different data types
#str() - any data to string
#int() - any data to integer

print(20 + int("20"))
print(20 + age + .09)

#input method will allow intereaction with terminal and pass values
#input() is like prompt in Js but for terminal
#print(input("Enter your age here: "))
#print(string + string) will push them together not actually calculate

new_age = input("Enter your new age: ")
print(f"You're now {new_age} years old.")

x = int(input("Enter x value:"))
y = int(input("Enter y value:"))
print(x + y)