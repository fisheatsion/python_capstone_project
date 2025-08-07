# Menu of snacks and drinks
menu = {
    1: {"name": "Candy Bar", "price": 1.50},
    2: {"name": "Soft Drink", "price": 3.50},
    3: {"name": "Cup Cake", "price": 2.50},
    4: {"name": "Water", "price": 2.00},
}

def display_menu():
    print("\nVending Machine Menu:")
    print("--------------------")
    for number, item in menu.items():
        print(number, ":", item["name"], "-", item["price"])
    print("--------------------")

# Track selected items and total cost
selected_items = []
total_cost = 0.0

# Display menu initially
display_menu()

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
            print("Added", name, price)
            display_menu()  # Display menu again after selection
        else:
            print("Invalid number Selected.")   # if selected number is out of range of the menu
            display_menu()  # Display menu again after invalid input to show what to choose
    else:
        print("Enter a valid number or 'done'.")
        display_menu()  # Display menu again after invalid input

# Print the receipt
print("\n" + "=" * 22)
print("Receipt".center(22))
print("=" * 22)
for item in selected_items:
    # Get the correct price for each item
    price = next((v["price"] for k, v in menu.items() if v["name"] == item), 0)
    print(f"{item} ${price:.2f}")
print("--------------------")    
print(f"Total cost: ${total_cost:.2f}")
print("====================")