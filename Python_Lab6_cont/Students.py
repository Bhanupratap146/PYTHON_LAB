class Student:
    def __init__(self, name, marks):  # Fixed method name
        self._name = name
        self._marks = marks
    def update_marks(self, new_marks):
        if 0 <= new_marks <= 100:  # Simplified condition
            self._marks = new_marks
            print(f"Marks updated to: {self._marks}")
        else:
            print("Invalid marks. Please enter a value between 0 and 100.")
    def display_student_info(self):
        print(f"Student Name: {self._name}")
        print(f"Marks: {self._marks}")
# Example usage
student1 = Student("John Doe", 85)  # No errors now
student1.display_student_info()
student1.update_marks(90)
student1.display_student_info()
