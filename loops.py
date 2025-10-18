# While loop repeating until a condition is met or a break statement is encountered infinite loop = True 
#count =1 #
#while count <=5:
      
#    print("Count is:", count+1)
#    count = +1

    # Break statement example
#    count=1
 #   while count <= 10: # loop until count is 10
  #      if count == 5: # when count is 5, break the loop
   #        print("Breaking the loop")
    #    break
     #   print("Count is:", count)
      #  count += 1            


        # Using continue statement to skip an iteration
#count = 0
#while count < 5:
 #   count += 1
  #  if# count == 3: # when count is 3, skip the rest of the loop and continue with next iteration
   #     print("Skipping number 3")
    #    continue
    #print("Count is:", count)   

    # Using else with while loop the else block executes when the while loop condition becomes false
#count = 1
#while count <= 3:
##  count += 1
#else:
#    print("Count has exceeded 3, exiting loop.")


# print("\n" + "="*60)
# print("PASSWORD CHECKER MINI CHALLENGE") 
# print("="*60)
# #Password checker using while loop

# correct_password = "secret123"
# access_granted = False

# while not access_granted:
#     user_input = input("Enter the password: ")
    
#     if user_input == correct_password:
#         print("Access Granted!")
#         access_granted = True
#     else:
#         print("Sorry, try again!")

# # For loops is used to iterate over a sequence (like a list, tuple, dictionary, set, or string)
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print("Fruit:", fruit)  

#     #looping through a string
# message = "Hello, Neo!"
# for char in message:
#     print("Character:", char)   

#     # Looping through a range of numbers
# for number in range(1, 6):  # from 1 to 5
#     print("Number:", number)   

#     # Using else with for loop the else block executes when the for loop completes all iterations
# else:
#     print("Finished looping through numbers.")
#     # Step skips numbers in the range
# for even_number in range(2, 11, 2):  # from 2 to 10 with step of 2
#     print("Even Number:", even_number)  
#     # Else in for loop 
#     for x in range(3):
#         print("x is:", x)   
#     else:
#         print("Looped through all x values.")

# # Break and continue in for loops
# for x in range(10):
#     if x == 5:
#         continue
#         print("Breaking the loop at x =", x)
#     if x
#         break
#     print("x is:", x)
# Mini-challenge: Count how many words have 5 or more letters

print("\n" + "="*60)
print("WORD LENGTH COUNTER CHALLENGE")
print("="*60)

# Create a list with 10 words
words = ["cat", "elephant", "dog", "butterfly", "sun", "computer", "tree", "mountain", "car", "adventure"]

print("List of words:", words)
print()

# Use a for loop to count words with 5 or more letters
count_long_words = 0

print("Checking each word:")
for word in words:
    print(f"'{word}' has {len(word)} letters", end=" - ")
    if len(word) >= 5:
        print("5+ letters ✓")
        count_long_words += 1
    else:
        print("Less than 5 letters")

print()
print(f"Total words with 5 or more letters: {count_long_words}")