#class method
# A class method is a method that is bound to the class and not the object of the class. It can modify a class state that applies across all instances of the class. A class method takes cls as the first parameter while a static method needs no specific parameters.
class Student:
    school_name = "ABC School"
    
    def __init__ (self, name, marks):
        self.name = name
        self.marks = marks
    
    @classmethod #decorator
    def change_school(cls, new_school_name): 
        cls.school_name = new_school_name
    
    def get_avg(self):
        sum = 0
        for mark in self.marks:
            sum += mark
        return sum/len(self.marks)

s1 = Student("Siddhesh", [95, 86, 90])
print(s1.name, s1.marks)
print("Average marks are:", s1.get_avg())
print("School name is:", Student.school_name)
Student.change_school("XYZ School") #changing school name using class method
print("New school name is:", Student.school_name)