# Create a sample dictionary
student_grades = { 
    "Alice": 90,
    "Bob": 85,
    "Charlie": 78,
    "David": 92
}

# Check if any grade is above 90 using a while loop
found_high_grade = False
for grade in student_grades.values():
    if grade > 90:
        found_high_grade = True
        break

# Print the result
if found_high_grade:
    print("High grade found!")
else:
    print("No high grades in the dictionary.")