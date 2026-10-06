students = {
    101: {"name": "Ram", "age": 20, "course": "Python"},
    102: {"name": "Sita", "age": 21, "course": "Java"},
    103: {"name": "Hari", "age": 19, "course": "Python"}
}

# 1. Display all students
for sid, info in students.items():
    print(sid, info)

# 2. Details of student 102
print("\nStudent 102:", students[102])

# 3. Change student 103's course
students[103]["course"] = "Data Science"

# 4. Add student 104
students[104] = {"name": "Gita", "age": 22, "course": "Java"}

# 5. Remove student 101
del students[101]

# 6. Final dictionary
print("\nFinal database:")
for sid, info in students.items():
    print(sid, info)

# Challenge
sid = int(input("\nEnter a student ID: "))
if sid in students:
    s = students[sid]
    print("Name:", s["name"])
    print("Age:", s["age"])
    print("Course:", s["course"])
else:
    print("Student not found.")