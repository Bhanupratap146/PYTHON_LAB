class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating objects for different students
student1 = Student("Ajay", 20)
student2 = Student("Abhinav", 21)
student3 = Student("Vijay", 19)

# Displaying information for each student
student1.display_info()
student2.display_info()
student3.display_info()
