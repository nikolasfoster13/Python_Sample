import inflect
# Define inflect engine
p = inflect.engine()
# Create list
names = []
while True:
    try:
        # Prompt user for name
        name = input("Name: ")
    except EOFError:
        # If user ctrl+d then stop prompting
        break
    else:
        # For each name provided, add to list
        names.append(name)
# Print blank line for aesthetic
print("")
# Print adieu adieu + , and names
print(f"Adieu, adieu, to {p.join(names)}")
