class Employee:
    def _init_(self, name, age, salary):
        self.name = name
        self._age = age
        self.__salary = salary
    def display_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Age: {self._age}")
        print(f"Salary: {self.__salary}")
    def _update_salary(self, new_salary):
        if new_salary >= 0:
            self.__salary = new_salary
            print(f"Salary updated to: {self.__salary}")
        else:
            print("Invalid salary. Salary cannot be negative.")
    def __set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary. Salary must be positive.")
    def get_salary(self):
        return self.__salary
    def set_salary(self, salary):
        self.__set_salary(salary)
employee = Employee("John Doe", 30, 50000)
employee.display_details()
print(f"Employee Name (public): {employee.name}")
employee.name = "Jane Doe"
print(f"Updated Employee Name: {employee.name}")
print(f"Employee Age (protected): {employee._age}")
employee._age = 31  
print(f"Employee Salary (via getter): {employee.get_salary()}")
employee.set_salary(55000)
print(f"Employee Salary (after setter): {employee.get_salary()}")
