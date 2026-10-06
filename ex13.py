employee = {
    "name": "John",
    "age": 30,
    "department": "IT",
    "salary": 50000,
    "city": "Kathmandu"
}

del employee["age"]        # remove using del
employee.pop("city")       # remove using pop()

print(employee)

# Safely try to remove "email"
removed = employee.pop("email", None)
if removed is None:
    print("email key not found")