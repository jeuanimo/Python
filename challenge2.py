#MINI-CHALLENGE - Subtraction Function

#Create Function and parameters
print("***************** Subtraction Calculator ***************************************")
def subtraction(num1, num2):
    return num1 - num2

# Use input statements to gather the numbers from the user
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# Assign the function to a variable and pass two numbers to the function
results = subtraction(first_number, second_number)

# Print the variable
print(f"The result of {first_number} - {second_number} = {results}")
print(results)