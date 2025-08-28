class Student:
    def __init__ (self, name, marks):
        self.name = name
        self.marks = marks
    
    @staticmethod #decorator
    def hello():
        print("Hello")

    def get_avg(self):
        sum = 0
        for mark in self.marks:
            sum += mark
            return sum/ len(self.marks)
        
    
s1 = Student("Siddhesh", [95, 86, 90])
print(s1.name, s1.marks)
print("Average marks are:", s1.get_avg())
Student.hello()