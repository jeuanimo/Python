# Dictionaries are mutable mappings in Python that store key-value pairs. They are defined using curly braces {}.
students = {
    "name": "Jeuan",
    "age": 54,
    "major": "computer science"
}
print("Student dictionary:", students)

# Accessing values using keys
print("Name:", students["name"])
print("Major:", students.get("major"))

# Adding a new key-value pair
students["graduation_year"] = 1996
print("After adding graduation year:", students)
# Updating an existing value
students["age"] = 55        
print("After updating age:", students)
# Removing a key-value pair
students.pop("major")
print("After removing major:", students)
# Check if a key exists
if "name" in students:
    print("Name key exists in the dictionary.")

    # Nested dictionary
    students = {
        "student1": {"name": "Jeuan", "age": 54},
        "student2": {"name": "Alicia", "age": 22},
    }
    print("\nNested student dictionary:", students)
    print("Student1's name:", students["student1"]["name"])

print("\n################################ MINI CHALLENGE ################################")

#### Challenge: Create a report card dictionary

# Create a dictionary called report_card with keys: name, subject, grade (using a tuple with 3 numbers)
report_card = {
    "name": "Thomas Anderson",
    "subject": "Hacking 101", 
    "grade": (85, 92, 78)
}

print("Report Card:", report_card)
print("Student Name:", report_card["name"])
print("Subject:", report_card["subject"])
print("Individual Grades:", report_card["grade"])

# Calculate the average of the three numbers in the grade tuple
grade_tuple = report_card["grade"]
average = sum(grade_tuple) / len(grade_tuple)
print(f"Calculated Average: {average:.2f}")

# Add a new key called "average" with calculated results
report_card["average"] = average
print("Updated Report Card:", report_card)

# Grade evaluation based on average
if report_card["average"] >= 90:
    print("Excellent, Neo!")
elif report_card["average"] >= 70:
    print("Good Job, Neo!")
else:
    print("See me after class, Neo!") 

     # Remove decimal points from average and update the dictionary
report_card["average"] = int(report_card["average"])
print("Final Report Card:", report_card)
print("Final Average (no decimals):", report_card["average"])
print("End of dictionaries.py")
# Rounding function
def round_grade(grade):
    return int(grade + 0.5)
print("Rounded Grade:", round_grade(average))
# :.2f for formatting to 2 decimal places
print(f"Formatted Average to 2 decimal places: {average:.2f}")      
#.0f for formatting to no decimal places
print(f"Formatted Average to no decimal places: {average:.0f}")