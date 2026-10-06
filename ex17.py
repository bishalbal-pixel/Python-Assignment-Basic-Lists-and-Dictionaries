fruits = [
    "apple", "banana", "apple",
    "orange", "banana", "apple",
    "mango", "orange", "banana"
]

count = {}

for fruit in fruits:
    if fruit in count:
        count[fruit] += 1    # seen before: add 1
    else:
        count[fruit] = 1     # first time: start at 1

print(count)