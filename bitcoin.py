import requests
import sys
import json

while True:
    try:
        if len(sys.argv) != 2:
            sys.exit("Missing command-line argument")

        elif int(sys.argv[1]) < 1:
            raise ValueError

        else:
            response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=297fee44b270cbe1131a8e7b158dd23fec0805dbd5ea83cd57653010dcb7baa6")
            o = response.json()
            price = o["data"]["priceUsd"]
            cost = float(sys.argv[1]) * float(price)
            sys.exit(f"${cost:,.4f}")

    except ValueError:
        sys.exit("Command-line argument is not a number")

