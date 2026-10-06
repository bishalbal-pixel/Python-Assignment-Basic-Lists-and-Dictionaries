marks = {
    "Ram": 75,
    "Sita": 88,
    "Hari": 65,
    "Gita": 92,
    "John": 55
}

for name, mark in marks.items():
    print(name, "-", mark)

total = sum(marks.values())
print("Total:", total)
print("Average:", total / len(marks))
print("Highest:", max(marks.values()))
print("Lowest:", min(marks.values()))

top_student = max(marks, key=marks.get)
print("Top student:", top_student)