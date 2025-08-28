class Studen:
    college_name = "ABC College"
    name = "Siddhesh" #class attribute

    def __init__(self, name, marks):
        self.name = name #object attribute > class attribugte
        self.marks = marks
        print("Adding students details...")
    
s1 = Studen("Siddhesh", 85)
print(s1.name, s1.marks, s1.college_name)