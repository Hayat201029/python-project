# ATM Management System

PIN = "1234"
balance = 10000

print("===== Welcome to ATM =====")

user_pin = input("Enter your 4-digit PIN: ")

if user_pin == PIN:
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"Your Balance: Rs. {balance}")

        elif choice == "2":
            amount = float(input("Enter deposit amount: "))
            if amount > 0:
                balance += amount
                print("Deposit Successful!")
                print("New Balance:", balance)
            else:
                print("Invalid amount!")

        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))
            if amount <= balance and amount > 0:
                balance -= amount
                print("Please collect your cash.")
                print("Remaining Balance:", balance)
            else:
                print("Insufficient balance or invalid amount!")

        elif choice == "4":
            print("Thank you for using our ATM.")
            break

        else:
            print("Invalid choice! Please try again.")

else:
    print("Incorrect PIN. Access Denied.")