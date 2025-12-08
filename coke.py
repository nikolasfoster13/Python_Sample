# Informs user of cost
print("Amount Due: 50")
# Lists valid USD coins
valid_coins = {5, 10, 25, 50}
# Sets starting amount to 0
inserted = 0

while True:
    # Prompts user for coin
    coin = int(input("Insert Coin: "))

    #Checks if coin is valid
    if coin in valid_coins:
        # If valid, add to balance
        inserted += coin

    else:
        # If invalid, reprompt for coin
        coin = int(input("Insert Coin: "))
        inserted += coin

    if inserted < 50:
        # If inserted amount is less than 50, inform user of remaining balance
        print(f"Amount Due: {50 - inserted}")

    elif inserted > 50:
         # If inserted amount is greater than 50, inform user of change due
         print(f"Change Owed: {inserted - 50}")
         break

    else:
        # If inserted amount is equal to 50, inform user no change due
        print("Change Owed: 0")
        break


