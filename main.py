# Python Data Structures & Functions Demo

# 1. LIST
students = ["Vidya", "Riya", "Neha", "Priya"]

print("LIST")
print("Students:", students)

students.append("Aisha")
print("After adding:", students)

print()


# 2. TUPLE
subjects = ("Python", "Java", "Database", "Networking")

print("TUPLE")
print("Subjects:", subjects)
print("First subject:", subjects[0])

print()


# 3. DICTIONARY
student = {
    "name": "Vidya",
    "age": 22,
    "course": "MCA",
    "university": "Atmiya University"
}

print("DICTIONARY")
print("Student:", student)

print()


# 4. KEY-VALUE PAIRS
print("KEY-VALUE PAIRS")

for key, value in student.items():
    print(key, ":", value)

print()


# 5. FUNCTION
def calculate_total(marks):
    return sum(marks)


marks = [80, 75, 90, 85, 70]

total = calculate_total(marks)

print("FUNCTION")
print("Marks:", marks)
print("Total:", total)