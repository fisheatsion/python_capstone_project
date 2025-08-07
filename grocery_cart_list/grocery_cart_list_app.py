# 2. Simple Grocery Cart Checkout
# Write a program that:
# Has a predefined dictionary of groceries with prices.
# Lets the user “add” items by typing their names.
# For each valid item, asks for the quantity.
# Keeps adding to the cart until the user types "checkout".
# Displays a final bill: each item, quantity, subtotal, and total.
# Skills practiced: dictionaries, loops, input(), math operations, formatting, error handling
def grocery_cart():
    # Predefined grocery items with prices
    groceries = {
        "apple": 50.50,
        "banana": 2.59,
        "milk": 40.49,
        "bread": 10.00,
        "eggs": 21.50,
        "cheese": 5.99,
        "chicken": 700.00,
        "rice": 190.50,
        "pasta": 65.49,
        "tomato": 20.65
    }
    
    # Initialize shopping cart
    cart = {}
    
    print("\nWelcome to the Grocery Store!")
    print("Available items:""\n", ", ".join(groceries.keys()))
    print("Type 'checkout' when you're done shopping.\n")
    
    # Main shopping loop
    while True:
        # Get item name from user
        item = input("Enter item name to add to cart: ").strip().lower()
        
        # Check for checkout command
        if item == "checkout":
            break
        
        # Validate item exists and show avilable item in
        if item not in groceries:
            print(f"Sorry, we don't have '{item}'. Available items:", ", ".join(groceries.keys()))
            continue
        
        # Get quantity from user 
        while True:
            try:
                quantity = int(input(f"How many {item}s would you like? "))
                if quantity <= 0:
                    print("Please enter a positive number.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
        
        # Add to cart or update quantity if already in cart
        if item in cart:
            cart[item]["quantity"] += quantity
        else:
            cart[item] = {
                "quantity": quantity,
                "price": groceries[item]
            }
        
        print(f"Added {quantity} {item}(s) to your cart.")
    
    # Check if cart is empty
    if not cart:
        print("\nYour cart is empty. Goodbye!")
        return
    
    # Generate and display bill
    print("\n\n============== Your Grocery Bill =================")
    print("{:<15} {:<10} {:<10} {:<10}".format("Item", "Price", "Quantity", "Subtotal"))
    print("-" * 45)
    
    total = 0
    for item, details in cart.items():
        subtotal = details["price"] * details["quantity"]
        total += subtotal
        print("{:<15} ETH.{:<9.2f} {:<10} ETH.{:<9.2f}".format(
            item.capitalize(), 
            details["price"], 
            details["quantity"], 
            subtotal
        ))
    
    print("-" * 45)
    print("{:<15} {:<10} {:<10} ETH.{:<9.2f}".format("", "", "TOTAL:", total))
    print("\nThank you for shopping with us!")
    print("-" * 45)

# Run the grocery cart program
grocery_cart()