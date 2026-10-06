contacts = {
    "Ram": "9841000000",
    "Sita": "9851000000",
    "Hari": "9861000000"
}

while True:
    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display Contacts")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        name = input("Enter name: ")
        if name in contacts:
            print("Contact already exists.")
        else:
            contacts[name] = input("Enter phone number: ")
            print("Contact added.")

    elif choice == "2":
        name = input("Enter name to search: ")
        if name in contacts:
            print(name, "-", contacts[name])
        else:
            print("Contact not found.")

    elif choice == "3":
        name = input("Enter name to update: ")
        if name in contacts:
            contacts[name] = input("Enter new phone number: ")
            print("Contact updated.")
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == "5":
        if contacts:
            for name, phone in contacts.items():
                print(name, "-", phone)
        else:
            print("No contacts saved.")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1 to 6.")