def main():
    # Prompt user for cost of meal
    dollars = dollars_to_float(input("How much was the meal? "))
    # Prompt user for tip percentage
    percent = percent_to_float(input("What percentage would you like to tip? "))
    # Calculate tip amount
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollars):
    # Remove dollar sign and converts to float
    return float(dollars.replace("$",""))


def percent_to_float(percent):
    # Remove percent sign and converts to float
    return float(percent.replace("%",""))/100

main()
