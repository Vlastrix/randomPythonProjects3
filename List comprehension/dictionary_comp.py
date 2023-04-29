import random
import pandas
# to remember
# new_dict = {new_key:new_value for item in list if something is true}

names = ["Alex", "Beth", "Vlad", "Caroline", "Dave"]

student_scores = {student: random.randint(50, 100) for student in names}
print(student_scores)
# print(student_scores.items())
# to remember
# new_key: new:value for (key: value) in dictionary.items() if something is true
passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}

print(passed_students)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries with normal for loops:
for (key, value) in student_dict.items():
    print(value)

student_dt = pandas.DataFrame(student_dict)

print(student_dt)

# Loop through a data frame
# for (key, value) in student_dt.items():
#     print(key)

# Loop through each of the rows
for (index, row) in student_dt.iterrows():
    print(row)