class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating two instances of the Person class
person1 = Person("Vijay", 21)
person2 = Person("Ajay", 26)

# Printing the name and age of each person
print(f"Name: {person1.name}, Age: {person1.age}")
print(f"Name: {person2.name}, Age: {person2.age}")
