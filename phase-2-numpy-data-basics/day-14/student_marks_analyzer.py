import numpy as np 

# 5 students 3 sub marks Math | Science | English
students_marks = np.array([
    [78,67,93],
    [87,59,86],
    [67,89,74],
    [86,88,83],
    [97,59,85]
])

print("Student Marks Dataset:\n", students_marks)

#avf marks
avg_marks = np.mean(students_marks)
print("Student avg Marks :\n", avg_marks)

#highest marks
highest_marks = np.max(students_marks)
print("Highest Score:\n", highest_marks)

#lowest marks
lowest_marks = np.min(students_marks)
print("Lowest Score:\n",lowest_marks )

#sub wise avg
subject_avg = np.mean(students_marks, axis=0)
print("Subject-wise average:\n", subject_avg)

#each student total marks
student_totals = np.sum(students_marks, axis=1)
print("Total marks per student:", student_totals)

#top student
top_student = np.argmax(student_totals)
print("Top student index:", top_student)
print("Top student marks:", student_totals[top_student])