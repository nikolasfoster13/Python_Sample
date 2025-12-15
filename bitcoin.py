import requests
import sys
import json

while True:
    try:
        # Ensure command-line argument has 1 parameter
        if len(sys.argv) != 2:
            # Inform user of missing command-line argument and exit
            sys.exit("Missing command-line argument")

        else:
            # Call coincap API for current price
            response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=297fee44b270cbe1131a8e7b158dd23fec0805dbd5ea83cd57653010dcb7baa6")
            # Format to JSON dict
            o = response.json()
            # Extract price from dict
            price = o["data"]["priceUsd"]
            # Multiply price by number prompt
            cost = float(sys.argv[1]) * float(price)
            # Print price formatted with , sep thousands to 4 decimals
            print(f"${cost:,.4f}")
            sys.exit()

    # If CL argument is non numeric, return error and exit
    except ValueError:
        sys.exit("Command-line argument is not a number")

