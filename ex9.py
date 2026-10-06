numbers = [10, 20, 10, 30, 20, 40, 10, 50, 30]
unique = []

for n in numbers:
    if n not in unique:
        unique.append(n)

print(unique)