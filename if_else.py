# If-Else Statements in Python
# If-Else statements are used to perform different actions based on different conditions.
# if- checks a condition and executes a block of code if the condition is true.
# elif- checks another condition if the previous condition is false.
# else- executes a block of code if the condition is false. 


age=23

if age < 100:
    if age < 21:
        print("You are a minor without access")
    
    else:
        print("You are young")
elif age == 100:
    print("Congratulations! You are a century old")
else:
    print("Sorry,You are old")

# Nested If-Else Statements

x=0

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")  

# shorthand If-Else Statement (Ternary Operator)
y=1
if y > 5:
    print("y is greater than 5")


# Ternary Operator
result = "y is greater than 5" if y > 5 else "y is 5 or less"
print(result)

# Nested if Statements
e=15
if e > 0:
    if e > 20:
        print("e is a positive number less than 20")
# combining conditions using logical operators
    if age < 21 and age <= 26:
        print("You are between 21 and 26")

f = 8
k = 8
if f == k:
    print("Hello")
else:
    print("Welcome")
    