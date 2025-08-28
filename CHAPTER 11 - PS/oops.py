# #class
# class Student:
#     name = "Siddhesh"

# # creating the object (instance)
# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)

#Default constructor
def __init__(self):
    print("This is deafault constructor")

#parameterized constructor
class Car:
    def __init__(self, name, model, year):
        print("Car details are as follows: ")
        self.name = name
        self.model = model
        self.year = year

c1 = Car("BMW", "X5", "2025")
print(print("The name of car is:",c1.name))
print(c1.model)
print(c1.year)
