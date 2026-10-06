students = ["Ram", "Sita", "Hari", "Gita"]
marks = {"Ram": 75, "Sita": 88, "Hari": 65, "Gita": 92}

for name in students:
    print(name, "-", marks[name])

print("\nScored 80 or above:")
for name in students:
    if marks[name] >= 80:
        print(name, "-", marks[name])