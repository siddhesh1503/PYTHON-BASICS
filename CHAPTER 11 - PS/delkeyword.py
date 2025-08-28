#del keyword is used to delete the reference of a variable.
class Student:
    def __init__ (self, name, marks):
        self.name = name
        self.marks = marks

s1 = Student("Siddhesh", [95, 86, 90])

print(s1.name, s1.marks)
del s1.marks
print(s1.name)
#print(s1.marks) #AttributeError: 'Student' object has no attribute 'marks'