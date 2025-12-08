# Prompt user for a string
user = input("Please provide a string: ")
# Create dictionary that coorelates vowels to blanks
vowels = {"A":"","a":"","E":"","e":"","I":"","i":"","O":"","o":"","U":"","u":""}
# Variable to represent fresh start
blank = ""
# For letters in the input
for char in user:
    # If the letter is vowel
    if char in vowels:
        # Return the definition of the vowel
        blank+=vowels[char]
    # If the letter is a consonant
    else:
        # Return the original letter
        blank += char
# Display updated string
print(blank)
