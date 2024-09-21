# Create a sample dictionary of student grades
student_grades = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 78,
    "David": 92
}

# Check if any grade is above 90 using a while loop
found_high_grade = False
grades = student_grades.values()  # Get all grades

# Iterate through the grades
iterator = iter(grades)
while not found_high_grade:
    grade = next(iterator)
    if grade > 90:
        found_high_grade = True
    

# Print the result
if found_high_grade:
    print("High grade found!")
else:
    print("No high grades in the dictionary.")