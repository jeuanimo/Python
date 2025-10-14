#functions are blocks of code that run when called
def my_function():
    print("This is my function.")
#call functions
my_function()
#function with parameters
def print_full_name(fname, last_name):
    print(f"This is my full name: {fname} {last_name}")

#function that returns something
def get_full_name(fname, last_name):
    return f"{fname} {last_name}"

#store the returned value in a variable
full_name = get_full_name("Jeuan", "Mitchell")
print(full_name)

"""#MINI-CHALLENGE

#Create Function and parameters
def subtraction(num1, num2):
    return num1 - num2

#Call function
results = subtraction(17, 8)

#Print function
print(results)"""

def combine_words(word1, word2, word3):
    combine = word1 + " " + word2 + " " + word3
    return combine

result = combine_words("HELLO", "WORLD", "I'M BOB!")
print(result)

def future_age(current_age):
    return current_age + 10

age_in_10 = future_age(28)
print(f"Age in 10 years: {age_in_10}")

def check_even(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")

check_even(7)
check_even(12)

def count_letters(word):
    return len(word)

letters = count_letters("Salutations")
print(f"There are {letters} letters.")