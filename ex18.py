product = {
    "name": "Laptop",
    "brand": "Dell",
    "price": 75000,
    "quantity": 5
}

print("Product:", product["name"], "-", product["brand"])
print("Price:", product["price"])
print("Quantity:", product["quantity"])

total_value = product["price"] * product["quantity"]
print("Total value:", total_value)

# Sell 2 laptops
product["quantity"] -= 2
print("\nAfter selling 2 laptops:")
print("Quantity:", product["quantity"])
print("Total value:", product["price"] * product["quantity"])