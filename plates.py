def main():
    # Prompts user for a license plate
    plate = input("Plate: ")
    # If plate is valid
    if is_valid(plate):
        print("Valid")
    # If plate is invalid
    else:
        print("Invalid")


def is_valid(s):

    # Return False if first 2 char are numeric
    if not s[0:2].isalpha():
        return False

    # Return False if total length less than 2 or greater than 6 char
    if not 2 <= len(s) <= 6:
        return False

    # Return False if plate is not alpha numeric
    if not s.isalnum():
        return False

    # Defines numeric values in the strings as "."
    numbers = {"0":".",
               "1":".",
               "2":".",
               "3":".",
               "4":".",
               "5":".",
               "6":".",
               "7":".",
               "8":".",
               "9":"."}
    # Assigns starting variable
    blank = ""
    # For characters in the plate
    for char in s:
        # If the character is numeric, replace it with "."
        if char in numbers:
            blank+=numbers[char]
        # If the character is not numeric, return the character
        else:
            blank+=char
    # Split the new string on "."
    parts = blank.split(".")
    # Separates the alpha parts
    alpha_parts = [p for p in parts if p]
    # If the length of the list is > 1, return false
    if len(alpha_parts) > 1:
        return False
    # Defines 0 as "."
    leading_zero = {"0":"."}
    # Assigns starting variable
    blank = ""
    # For characters in the plate
    for char in s:
        # If the character is 0, replace with "."
        if char in leading_zero:
            blank+=numbers[char]
        # If the character is not 0, return the character
        else:
            blank+=char
    # Split the new string on "."
    parts = blank.split(".")
    # Creates a list of the parts
    alpha_parts = [p for p in parts if p]
    # If the length of the list is at least 2, it was split, check if the first part of the list is alpha only
    if len(alpha_parts) > 1 and alpha_parts[0].isalpha():
        return False
    else:
        return True

main()
