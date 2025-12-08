user = input("Please provide a string: ")
vowels = {"A":"","a":"","E":"","e":"","I":"","i":"","O":"","o":"","U":"","u":""}
blank = ""
for char in user:
    if char in vowels:
        blank+=vowels[char]
    else:
        blank += char
print(blank)
