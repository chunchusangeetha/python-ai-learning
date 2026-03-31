import json
import os

FILE = "student.json"

def read_data():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        try:
            return json.load(f)
        except:
            return []

def write_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_student():
    name = input("Enter your name: ")
    marks = int(input("Enter your marks: "))

    students = read_data()
    if any(s['name'].lower() == name.lower() for s in students):
        print(f"Error: Student '{name}' already exists!")
        return
    students.append({
        "name": name,
        "marks": marks
    })
    write_data(students)
    print("Student added successfully!")

def view_student():
    students = read_data()

    if not students:
        print("No students found!")
        return

    print("\n Student List:")
    for s in students:
        print(f"Name: {s['name']} , Marks: {s['marks']}")

def update_student_marks():
    students = read_data()

    if not students:
        print("No students available!")
        return

    target = input("Enter student name to update: ")
    found = False

    for s in students:
        if s['name'].lower() == target.lower():
            new_marks = int(input(f"Enter new marks for {s['name']}: "))
            s['marks'] = new_marks
            found = True
            break

    if found:
        write_data(students)
        print("Updated successfully!")
    else:
        print("Student not found!")

def delete_student():
    students = read_data()
    target = input("Enter the name of the student to delete: ").strip()
    
    original_count = len(students)
    students = [s for s in students if s['name'].lower() != target.lower()]
    
    if len(students) < original_count:
        write_data(students)
        print(f"Deleted student '{target}' successfully.")
    else:
        print(f"Student '{target}' not found.")

while True:
    print("\n1. Add  2. View  3. Update 4.Delete  5. Exit")
    choice = input("Choose: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_student()
    elif choice == '3':
        update_student_marks()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        break
    else:
        print("Invalid choice!")