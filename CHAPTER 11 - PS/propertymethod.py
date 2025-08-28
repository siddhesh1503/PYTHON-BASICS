# Property decorator
# A property decorator is used to define a method as a property. It allows you to access the method like an attribute, without needing to call it as a method. This is useful for creating read-only attributes or computed properties.
class Student:
    def __init__ (self, name, marks):
        self.name = name
        self.marks = marks
    
    @property #decorator
    def avg(self):
        sum = 0
        for mark in self.marks:
            sum += mark
        return sum/len(self.marks)

s1 = Student("Siddhesh", [95, 86, 90])
print(s1.name, s1.marks)
print("Average marks are:", s1.avg)
#print("Average marks are:", s1.get_avg()) --- IGNORE ---

marks = [95, 86, 90]
print("Average marks are:", sum(marks)/len(marks))
#Property decorator allows us to access avg method as an attribute without using parentheses.