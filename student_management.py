students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        students.append({"Name": name, "Roll No": roll})
        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            print("\nStudent List:")
            for student in students:
                print("Name:", student["Name"], "| Roll No:", student["Roll No"])

    elif choice == "3":
        roll = input("Enter roll number to search: ")
        found = False

        for student in students:
            if student["Roll No"] == roll:
                print("Student Found!")
                print("Name:", student["Name"])
                print("Roll No:", student["Roll No"])
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "4":
        roll = input("Enter roll number to delete: ")
        found = False

        for student in students:
            if student["Roll No"] == roll:
                students.remove(student)
                print("Student deleted successfully!")
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")