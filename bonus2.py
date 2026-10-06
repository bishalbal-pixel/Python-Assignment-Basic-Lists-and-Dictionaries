cart = ["apple", "banana", "apple", "mango"]
prices = {"apple": 100, "banana": 50, "mango": 150}

total = 0
for item in cart:
    total += prices[item]

print("Total =", total)