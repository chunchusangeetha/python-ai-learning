class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_salary(self, percentage):
        if percentage < 0:
            print("Invalid percentage! Please enter a positive value.")
        else:    
            self.salary += self.salary * (percentage / 100)
            print(f"Salary increased by {percentage}%. New salary: {self.salary}")

    def display(self):
        print(f"Employee Name: {self.name}, Salary: {self.salary}")

e1 = Employee("Bob", 50000)
e1.display()
e1.increase_salary(10)
e1.display()
