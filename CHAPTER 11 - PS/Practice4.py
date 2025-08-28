class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    
    @staticmethod
    def showDetails(self):
        print(f"Role is: {self.role}\nDepartment is: {self.dept}\nSalary is: {self.salary}")

e1 = Employee("Manager", "Sales", 50000)
Employee.showDetails(e1)
e2 = Employee("Developer", "IT", 60000)
Employee.showDetails(e2)