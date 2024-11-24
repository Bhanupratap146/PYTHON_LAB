class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self._age = age
        self.__salary = salary

    def display_details(self):
        print(f"Name: {self.name}, Age: {self._age}, Salary: {self.__salary}")

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
            print(f"Salary updated to: {self.__salary}")
        else:
            print("Invalid salary. Salary must be positive.")


# Example usage
employee = Employee("John Doe", 30, 50000)
employee.display_details()

employee.name = "Jane Doe"
print(f"Updated Name: {employee.name}")

employee._age = 31  # Direct access for protected attribute
print(f"Updated Age: {employee._age}")

print(f"Salary: {employee.get_salary()}")
employee.set_salary(55000)
print(f"Updated Salary: {employee.get_salary()}")
