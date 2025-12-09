# Dictionary for item/cost
menu ={"Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00}
# Declares starting point for customer cart
total = 0

while True:
    try:
        # Prompt user for item
        user = input("Item: ").title().strip()
        # If input exists on menu
        if user in menu:
            # Declare add variable as price of item
            total += menu[user]
            # Print running total
            print(f"Total: ${total:.2f}")
        # If user input is not on menu, reprompt for item
        else:
            pass
    # If user ends, break loop
    except EOFError:
        break



