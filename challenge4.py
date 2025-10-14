# Grade Checker v1.0 by Jeuan  

# Ask the user to enter a score between 0 and 100
score = int(input("Please enter a score between (0-100): "))

# Use if, elif, else to determine and print the grade
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# Print the result
print(f"Your score is {score} and your grade is: {grade}")

# Baby Flex :): validation and feedback
if score < 0 or score > 100:
    print("Warning: Score should be between 0 and 100!")
elif grade == "A":
    print("Excellent work!")
elif grade == "B":
    print("Good job!")
elif grade == "C":
    print("Average performance.")
elif grade == "D":
    print("Below average. Consider studying more.")
else:
    print("Failing grade. Please seek help and study harder. The fries will not bag themselves!")
