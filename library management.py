# Library Management System

library = {}

def add_book():
    book = input("Enter book name: ")
    quantity = int(input("Enter quantity: "))
    library[book] = quantity
    print("Book added successfully!\n")

def view_books():
    if not library:
        print("Library is empty.\n")
    else:
        print("\nAvailable Books:")
        for book, qty in library.items():
            print(f"{book} - {qty} copies")
        print()

def issue_book():
    book = input("Enter book name to issue: ")
    if book in library:
        if library[book] > 0:
            library[book] -= 1
            print("Book issued successfully!\n")
        else:
            print("Book is out of stock.\n")
    else:
        print("Book not found.\n")

def return_book():
    book = input("Enter book name to return: ")
    if book in library:
        library[book] += 1
    else:
        library[book] = 1
    print("Book returned successfully!\n")

while True:
    print("===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        print("Thank you for using Library Management System!")
        break
    else:
        print("Invalid choice! Try again.\n")