numbers = [45, 12, 78, 3, 56, 23, 89, 10]

# 1. Original list
print("Original:", numbers)

# 2. Ascending order (sorted() makes a NEW list)
print("Ascending:", sorted(numbers))

# 3. Descending order (sort() changes the ORIGINAL list)
numbers.sort(reverse=True)
print("Descending:", numbers)

# 4. Smallest number
print("Smallest:", min(numbers))

# 5. Largest number
print("Largest:", max(numbers))

# Sort names alphabetically
names = ["Sita", "Ram", "Hari", "Gita", "Anita"]
names.sort()
print("Names:", names)