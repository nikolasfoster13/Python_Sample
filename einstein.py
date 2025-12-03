# Explains program to user
print("This code will provide you the equivalent number of jules to the mass of an object.")

# Prompts user for mass of object
mass = input("What is the mass of your object in kilograms? (Please provide the numeric value) m = ")

# Casts user input as integer
int_mass = int(mass)

# Calculates energy
e = int_mass * 300000000 * 300000000

# Returns energy result to user
print(e)
