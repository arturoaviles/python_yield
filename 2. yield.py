import csv
from itertools import islice

filenames = ["students/students1A.csv", "students/students1B.csv"]

def get_student_grades(filenames):
    for each_file in filenames:
        with open(each_file, "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in islice(reader, 1, None):
                grade = int(row[2])
                yield grade

student_grades = get_student_grades(filenames)


total = sum([grade for grade in student_grades])

total_students = 0
for grade in get_student_grades(filenames):
    total_students = total_students + 1

print(total/total_students)




