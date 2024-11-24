class Student:
    def _init_(self, name, marks):
        self._name = name
        self._marks = marks
    def update_marks(self, new_marks):
        if new_marks >= 0 and new_marks <= 100:
            self._marks = new_marks
            print(f"Marks updated to: {self._marks}")
        else:
            print("Invalid marks. Please enter a value between 0 and 100.")
    def display_student_info(self):
        print(f"Student Name: {self._name}")
        print(f"Marks: {self._marks}")
student1 = Student("John Doe", 85)
student1.display_student_info()
student1.update_marks(90)
student1.display_student_info()
