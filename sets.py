
set1 = set("abcdefg")
set2 = set("adegjke")
set3 = set("aaaaaaa")

# print(set1)
# print(set1.add("h"))
# print(set1)
# print(set1.remove("h"))
# print(set1)
# print(set1.pop())
# print(set1)

# print(set1.intersection(set2))  # Returns a new set with elements common to both sets.
# print(set1.union(set2))  # Returns a new set with elements from both sets.
# print(set1.difference(set2))  # Returns a new set with elements in set1 but not in set2.
# print(set1.symmetric_difference(set2))  # Returns a new set with elements in either set1 or set2 but not both.
# # These operations do not change the original sets, they change the sets produced with the code is ran.
# set4 = set1.symmetric_difference(set2)
# print(set4)  # Prints the new set created by the symmetric_difference operation.
# print(set4.isdisjoint(set1)) # Returns True if set4 and set1 have no elements in common.
# print(set4.isdisjoint(set3)) # Returns True if set4 and set3 have no elements in common.

# 2a) Yes, sets are mutable because you can add or remove elements from them.
# 2b) No, sets are not ordered.
# 2c) No, sets are not indexable because they are unordered collections.
# 2d) Yes, sets are iterable because you can iterate over the elements of a set using a loop.
# 2e) Yes, you can determine the length of a set using the len() funciton.
# 2f) Yes, you can determine if a specific element is in a set using the keyword "in".

# 3) You can differentiate sets and dictionaries with the are explicitly labeled by how they print. Sets have commas while dictionaries have colons.



s1 = set("abcdijklm")
s2 = set("defghijnop")
s3 = set("klmijnopqrst")

# print(s1.intersection(s2, s3))
# print(s1.difference(s2, s3))
# print(s2.intersection(s3))
# print(s1.intersection(s2).difference(s3))
# print((s1.intersection(s3).union(s2.intersection(s3))).difference(s1.intersection(s2, s3)))


# Read the data from the files
# with open("cs.txt", "r") as cs_file:
#     cs_majors = set(cs_file.read().splitlines())

# with open("math.txt", "r") as math_file:
#     math_majors = set(math_file.read().splitlines())

# # a. All of the math-cs double majors
# double_majors = cs_majors.intersection(math_majors)
# print("Math-CS Double Majors:", double_majors)

# # b. All of the people majoring in math or cs
# all_majors = cs_majors.union(math_majors)
# print("All Math or CS Majors:", all_majors)

# # c. All of the people who are strictly CS majors
# strictly_cs_majors = cs_majors.difference(math_majors)
# print("Strictly CS Majors:", strictly_cs_majors)

# Read the data from the files
# with open("cs.txt", "r") as cs_file:
#     cs_majors = set(cs_file.readlines()[1:])  # Skip the first line

# with open("math.txt", "r") as math_file:
#     math_majors = set(math_file.readlines()[1:])  # Skip the first line

# # a. All of the math-cs double majors
# double_majors = cs_majors.intersection(math_majors)
# print(cs_majors.intersection(math_majors))
# print("Math-CS Double Majors:", double_majors)

# # b. All of the people majoring in math or cs
# all_majors = cs_majors.union(math_majors)
# print("All Math or CS Majors:", all_majors)

# # c. All of the people who are strictly CS majors
# strictly_cs_majors = cs_majors.difference(math_majors)
# print("Strictly CS Majors:", strictly_cs_majors)

# Read the data from the files
# with open("cs.txt", "r") as cs_file:
#     cs_majors = set(line.strip() for line in cs_file.readlines()[1:]) 
#     print(cs_majors) # Skip the first line and strip newlines

# with open("math.txt", "r") as math_file:
#     math_majors = set(line.strip() for line in math_file.readlines()[1:])  # Skip the first line and strip newlines

# # a. All of the math-cs double majors
# double_majors = cs_majors.intersection(math_majors)
# # print("Math-CS Double Majors:", double_majors)

# # b. All of the people majoring in math or cs
# all_majors = cs_majors.union(math_majors)
# # print("All Math or CS Majors:", all_majors)

# # c. All of the people who are strictly CS majors
# strictly_cs_majors = cs_majors.difference(math_majors)
# # print("Strictly CS Majors:", strictly_cs_majors)

# # Read the data from the studentYear.txt file
# with open("studentYear.txt", "r") as year_file:
#     student_years = {line.split(",")[0].strip(): int(line.split(",")[1].strip()) for line in year_file.readlines()[1:]}

# # a. All sophomore level CS majors
# sophomore_cs_majors = {student for student in cs_majors if student_years.get(student) == 2}
# print("Sophomore CS Majors:", sophomore_cs_majors)

# # b. All freshmen who are not majoring in math or CS
# freshmen_not_math_cs = {student for student, year in student_years.items() if year == 1 and student not in all_majors}
# print("Freshmen not in Math or CS:", freshmen_not_math_cs)

# # c. All senior Math and CS majors
# senior_math_cs_majors = {student for student in math_majors.union(cs_majors) if student_years.get(student) == 4}
# print("Senior Math and CS Majors:", senior_math_cs_majors)

# Read the data from the studentYear.txt file
# with open("studentYear.txt", "r") as year_file:
#     student_years = {
#         line.split(",")[1].strip(): int(line.split()[0].strip())  # Split by space, extract year and name
#         for line in year_file.readlines()[1:]  # Skip the first line
#     }

# # a. All sophomore level CS majors
# sophomore_cs_majors = {student for student in cs_majors if student_years.get(student) == 2}
# print("Sophomore CS Majors:", sophomore_cs_majors)

# # b. All freshmen who are not majoring in math or CS
# freshmen_not_math_cs = {student for student, year in student_years.items() if year == 1 and student not in all_majors}
# print("Freshmen not in Math or CS:", freshmen_not_math_cs)

# # c. All senior Math and CS majors
# senior_math_cs_majors = {student for student in math_majors.union(cs_majors) if student_years.get(student) == 4}
# print("Senior Math and CS Majors:", senior_math_cs_majors)

with open("cs.txt", "r") as cs_file:
    cs_majors = set(line.strip() for line in cs_file.readlines()[1:]) 
    # print(cs_majors) # Skip the first line and strip newlines

with open("math.txt", "r") as math_file:
    math_majors = set(line.strip() for line in math_file.readlines()[1:])  # Skip the first line and strip newlines

double_majors = cs_majors.intersection(math_majors)
# print("Math-CS Double Majors:", double_majors)

all_majors = cs_majors.union(math_majors)
# print("All Math or CS Majors:", all_majors)

strictly_cs_majors = cs_majors.difference(math_majors)

# Read the data from the studentYear.txt file
with open("studentYear.txt", "r") as year_file:
    student_years = {}
    for line in year_file.readlines()[1:]:  # Skip the first line
        parts = line.split(",")
        if len(parts) == 2:  # Ensure the line has exactly two parts
            name = parts[1].strip()
            year = parts[0].strip().split()[0]  # Extract the year
            if year.isdigit():  # Ensure the year is a valid number
                student_years[name] = int(year)

# # a. All sophomore level CS majors
# sophomore_cs_majors = {student for student in cs_majors if student_years.get(student) == 2}
# print("Sophomore CS Majors:", sophomore_cs_majors)

# # b. All freshmen who are not majoring in math or CS
# freshmen_not_math_cs = {student for student, year in student_years.items() if year == 1 and student not in all_majors}
# print("Freshmen not in Math or CS:", freshmen_not_math_cs)

# # c. All senior Math and CS majors
# senior_math_cs_majors = {student for student in math_majors.intersection(cs_majors) if student_years.get(student) == 4}
# print("Senior Math and CS Majors:", senior_math_cs_majors)

# print("CS Majors:", cs_majors)
# print("Math Majors:", math_majors)
# print("Strictly CS Majors:", strictly_cs_majors)
# print("Student Years:", student_years)

# # Sophomore CS Majors
sophomore_cs_majors = {student for student in cs_majors if student_years.get(student) == 2}
print("Sophomore CS Majors:", sophomore_cs_majors)

# sophomore_cs_majors = set()
# for student in cs_majors:
#     if student_years.get(student) == 2:
#         sophomore_cs_majors.intersection(student)
# print("Sophomore CS Majors:", sophomore_cs_majors)

# Freshmen not in Math or CS
freshmen_not_math_cs = {student for student, year in student_years.items() if year == 1 and student not in all_majors}
print("Freshmen not in Math or CS:", freshmen_not_math_cs)

# Senior Math and CS Majors
senior_math_cs_majors = {student for student in math_majors.union(cs_majors) if student_years.get(student) == 4}
print("Senior Math and CS Majors:", senior_math_cs_majors)
