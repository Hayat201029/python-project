cart = []

def add_item():
    name = input("Enter Product Name: ")
    price = float(input("Enter Product Price: "))
    quantity = int(input("Enter Quantity: "))

    item = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    cart.append(item)
    print("Item added successfully!")

def view_cart():
    if not cart:
        print("Your cart is empty.")
        return

    total = 0

    print("\n----- Shopping Cart -----")
    for item in cart:
        subtotal = item["price"] * item["quantity"]
        total += subtotal

        print(f"Product : {item['name']}")
        print(f"Price   : {item['price']}")
        print(f"Quantity: {item['quantity']}")
        print(f"Subtotal: {subtotal}")
        print("-------------------------")

    print(f"Total Bill = {total}")

def remove_item():
    name = input("Enter Product Name to remove: ")

    for item in cart:
        if item["name"].lower() == name.lower():
            cart.remove(item)
            print("Item removed successfully!")
            return

    print("Item not found.")

def search_item():
    name = input("Enter Product Name to search: ")

    for item in cart:
        if item["name"].lower() == name.lower():
            print("\nItem Found")
            print("Product :", item["name"])
            print("Price   :", item["price"])
            print("Quantity:", item["quantity"])
            return

    print("Item not found.")

while True:
    print("\n===== Online Shopping Cart =====")
    print("1. Add Item")
    print("2. View Cart")
    print("3. Remove Item")
    print("4. Search Item")
    print("5. Checkout")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_item()

    elif choice == "2":
        view_cart()

    elif choice == "3":
        remove_item()

    elif choice == "4":
        search_item()

    elif choice == "5":
        view_cart()
        print("Thank you for shopping!")
        cart.clear()

    elif choice == "6":
        print("Program Closed.")
        break

    else:
        print("Invalid choice! Please try again.")