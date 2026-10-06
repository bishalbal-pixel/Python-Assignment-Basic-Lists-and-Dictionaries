marks = [75, 82, 68, 90, 55, 88, 72, 95]

def show_stats(marks):
    print("All marks:", marks)
    print("Total:", sum(marks))
    print("Average:", sum(marks) / len(marks))
    print("Highest:", max(marks))
    print("Lowest:", min(marks))

    count = 0
    for m in marks:
        if m >= 75:
            count += 1
    print("Students with 75 or more:", count)

    print("Highest to lowest:", sorted(marks, reverse=True))

show_stats(marks)

# Challenge
new_mark = int(input("\nEnter another student's mark: "))
marks.append(new_mark)
print("\nUpdated statistics:")
show_stats(marks)