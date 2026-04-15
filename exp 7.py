Demonstrate use of object- oriented programming concepts
aim:
To study and demonstrate the use of Object-Oriented Programming (OOP) concepts such as class, object, encapsulation, inheritance, polymorphism, and abstraction using Python.
Algorithm :
step 1 : Start 
step 2:Define a class (e.g., Student) with attributes and methods
step 3:Use constructor (__init__) to initialize values
step 4:Create objects of the class
step 5:Implement:
Encapsulation using private variables
Inheritance by creating a derived class
Polymorphism using method overriding
step 6:Call methods using objects
step 7:Display output
step 8 :End the program

#code
# Base class (Encapsulation)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age   # private variable
    def display(self):
        print("Name:", self.name)
        print("Age:", self.__age)
# Derived class (Inheritance)
class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks
    # Polymorphism (method overriding)
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
# Creating objects
p1 = Person("Ali", 30)
s1 = Student("Tasmiya", 20, 95)
# Calling methods
print("Person Details:")
p1.display()
print("\nStudent Details:")
s1.display()
