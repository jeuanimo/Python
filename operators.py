# Arithmetic Operators (Mathematical Operators)
# Assignment Operators (Assigning Values)
# Comparison Operators (Comparing Values)
# Logical Operators (Logical Operations)
# Identity Operators (Identity Checks)
# Membership Operators (Membership Checks List)

# Arithmetic Operators
x=1
y=2
res =0
res = x + y
print("Addition: ", res)
res = x - y
print("Subtraction: ", res) 
res = x * y
print("Multiplication: ", res)
res = x / y
print("Division: ", res)
res = x ** y
print("Exponent: ", res)    
res= x // y
print("Floor Division: ", res)
res = x % y
print("Modulus: ", res)
# Assignment Operators (Used to Assign Values to Variables)
x = 5
print("Value of x: ", x)
x += 5  # x = x + 5
print("New value of x: ", x)
x -= 3  # x = x - 3
print("New value of x: ", x)
x *= 3  # x = x * 3
print("New value of x: ", x)
x /= 3  # x = x / 3
print("New value of x: ", x)

# Comparison Operators (Used to Compare Two Values and Return a Boolean Result)
# ==(Equal to), !=(Not equal to), >(Greater than), <(Less than), >=(Greater than or equal to), <=(Less than or equal to)
if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")

# Logical Operators (Used to Combine Conditional Statements) and - both conditions should be true or - either condition should be true not - reverse the result
x=3
y = 3
z = 3
print(x==y and y==z) # False, both conditions are true
print(x==y or y!=z) # True, one condition is true
print(not(x==y and y==z))# False, reverse the result


if x > y and x > z:
    print("x is the greatest")
elif y > x and y > z:
    print("y is the greatest")
else:
    print("z is the greatest")

if x < y or x < z:
    print("x is the smallest")

# Identity Operators (Used to Compare the Memory Locations of Two Objects)
# is - returns True if both variables are the same object, is not - returns True if both variables are not the same object

x=3
y=3
print(x is y) # True, both variables are the same object
print(x is not y) # False, both variables are the same object

# Membership Operators (Used to Test if a Sequence is Present in an Object)
# in - returns True if a sequence with the specified value is present in the object, not in - returns True if a sequence with the specified value is not present in the object
print("---------------------------------------------------------------------")

# List
x=[1,2,3,4,5]
print(3 in x) # True, 3 is present in the list
print(6 not in x) # True, 6 is not present in the list

# List of Strings
fruits=["apple", "banana", "cherry"]
print(fruits[0])# True, "apple" is present in the list
print(fruits[2]) 
print(fruits[-1])

# Modify List
fruits[1] = "mango" # Change the value of the second item
print(fruits)   
# Add an item to the end of the list
fruits.append("orange")
print(fruits)
# Append a list to the end of the list
fruits.insert(1, "kiwi") # Insert "kiwi" at the second position
print(fruits)
# Remove a specific item from the list
fruits.remove("apple")
print(fruits)
# Remove the last item from the list
fruits.pop()
print(fruits)
# Check if an item is present in the list
if "mango" in fruits:
    print("mango is present in the list")
# List Length
print("Length of the list: ", len(fruits))
