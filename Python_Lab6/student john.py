class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

# Creating an instance of the Student class
student = Student("John", 2)

# Printing the name and roll number of the student
print(f"Name: {student.name}, Roll No: {student.roll_no}")
