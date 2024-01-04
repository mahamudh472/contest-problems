import random
class Employee:
    increment = 1.5
    def __init__(self, fname, lname, salery):
        self.fname = fname
        self.lname = lname
        self.selary = salery
    def increase(self):
        self.selary = self.selary * Employee.increment
    def gmail(self):
        return (self.fname+self.lname).lower()+str(random.randint(1,9)) + "@gmail.com"
mahamud = Employee("Mahamud", "Hasan", 5000)
mahamud.increase()
print(mahamud.selary)
print(mahamud.gmail())