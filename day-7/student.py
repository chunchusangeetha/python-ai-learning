class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display_details(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

    def update_marks(self,new_marks):
        if new_marks < 0 or new_marks > 100:
            print("Invalid marks! Please enter a value between 0 and 100.")
        else:
            self.marks = new_marks
            print(f"Marks updated to {self.marks} for {self.name}")

s1 = Student("Alice", 85)
s1.display_details()
s1.update_marks(90)
s1.display_details()                