# Student Marks Calculator
# Author: Karthik
# Description: Calculate total, average and grade of a student

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "Fail"


print("---- Student Marks Calculator ----")

name = input("Enter student name: ")

marks = []
subjects = ["Maths", "Science", "English", "Computer", "Social"]

for subject in subjects:
    score = int(input(f"Enter marks for {subject}: "))
    marks.append(score)

total = sum(marks)
average = total / len(marks)
grade = calculate_grade(average)

print("\n---- Result ----")
print("Student Name:", name)
print("Total Marks:", total)
print("Average:", average)
print("Grade:", grade)
