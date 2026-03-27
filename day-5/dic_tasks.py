user = {
  "name": "Sangeetha",
  "age": 25
}

print(user)

store = {}
name = input("Enter your name: ")
marks = int(input(f"Enter marks for {name}:"))

store[name] = marks
print(store)



def count_char(val):
    count_freq_char = {}
    for i in val:
        if i in count_freq_char:
            count_freq_char[i] += 1
        else:
            count_freq_char[i] = 1   

    
    return count_freq_char

print(count_char("sangeetha"))

def count_word(val):
    words = val.lower().split()
    count_word_dict = {}
    for word in words:
        if word in count_word_dict:
            count_word_dict[word] += 1
        else:
            count_word_dict[word] = 1   

    
    return count_word_dict

print(count_word("hey sangeetha how are you sangeeTHa"))

student_marks = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 90,
    "Diana": 88
}
highest_student = ""
highest_marks = 0
for name,score in student_marks.items():
    if score > highest_marks:
        highest_marks = score
        highest_student = name

print(f"Highest Marks: {highest_student} with {highest_marks}")   