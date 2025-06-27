# Menu of snacks and drinks
menu = {
    1: {"name": "Candy Bar", "price": 1.50},
    2: {"name": "Soft Drink", "price": 3.50},
    3: {"name": "Cup Cake", "price": 2.50},
    4: {"name": "Water", "price": 2.00},
}

# Display the menu
print("Menu:")
for number, item in menu.items():
    print(number, ":", item["name"], "-", item["price"])

# Track selected items and total cost
selected_items = []
total_cost = 0.0

# User input loop
while True:
    choice = input("Select item number or type 'done': ")
    
    if choice.lower() == "done":
        break
    if choice.isdigit():
        item_number = int(choice)
        if item_number in menu:
            name = menu[item_number]["name"]
            price = menu[item_number]["price"]
            selected_items.append(name)
            total_cost += price
            print("Added", name)
        else:
            print("Invalid number.")
    else:
        print("Enter a valid number or 'done'.")

# Print the receipt
print("\nReceipt:")
for name in selected_items:
    print(name)
print("Total cost:", total_cost)
