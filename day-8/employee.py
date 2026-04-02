class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

class Developer(Employee):
    def __init__(self,name,salary):
        super().__init__(name,salary)  

    def calculate_bonus(self,percentage=10):
        self.bonus = self.salary *(percentage/100)
        print(f"{self.bonus} of Developer")

class Manager(Employee):
    def __init__(self,name,salary):
        super().__init__(name,salary)  

    def calculate_bonus(self,percentage=20):
        self.bonus = self.salary *(percentage/100)
        print(f"{self.bonus} of Manager")

d1 = Developer("sangeetha",30000)
m1 = Manager("geetha",50000)
for x in (d1,m1):
    x.calculate_bonus()