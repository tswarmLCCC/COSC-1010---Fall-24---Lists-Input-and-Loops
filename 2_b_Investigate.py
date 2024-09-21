#Remember, you can either copy and paste these line by line into terminal to play with them, or highligh code blocks and run them with ctrl+enter
#This is demo'd in the video for this week if you need a reminder

### Investigate (Dictionaries in Python):
'''
1. **Accessing Values by Keys**:
   - Dictionaries allow you to store data with unique keys. You can access values using these keys.
   - In our example, we have a dictionary of student grades:
'''

student_grades = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 78,
    "David": 92
}
print(student_grades)


'''
   - To access Alice's grade, use `student_grades["Alice"]`.
   - Experiment with different keys and observe the corresponding values.

2. **Adding New Key-Value Pairs**:
   - Dictionaries are dynamic; you can add new data easily.
   - Suppose we want to add a new student name Emma's grade:
'''
student_grades["Emma"] = 88
print(student_grades)
'''
   - Now the dictionary includes Emma's grade.

3. **Modifying Existing Values**:
   - If a student's grade changes, update it directly:
'''
 
student_grades["Charlie"] = 80
print(student_grades) 
#   - Charlie's grade is now adjusted.
'''
4. **Removing Key-Value Pairs**:
   - To remove a student (e.g., Bob) and their grade:

 '''
del(student_grades["Bob"])
print(student_grades) 
'''
   - Bob's data is no longer in the dictionary.
'''
#Remember, dictionaries are like labeled drawers where you can store and retrieve information efficiently! 🗂️🔑📊