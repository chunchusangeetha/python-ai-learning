marks = int(input("Enter you marks: "))

if (marks >= 90):
    grade = 'A'
elif (marks >= 75):
    grade = 'B'
elif (marks >= 50):
    grade ='C'
else:
    grade = 'fail'   

print(f"your marks are {marks} so you got {grade}")
