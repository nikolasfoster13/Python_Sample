# Prompt user for camelCase input
user = input("What's your camelCase? ")

# Defines snake_case equivalent of capital letters
caps = {
    "A":"_a",
    "B":"_b",
    "C":"_c",
    "D":"_d",
    "E":"_e",
    "F":"_f",
    "G":"_g",
    "H":"_h",
    "I":"_i",
    "J":"_j",
    "K":"_k",
    "L":"_l",
    "M":"_m",
    "N":"_n",
    "O":"_o",
    "P":"_p",
    "Q":"_q",
    "R":"_r",
    "S":"_s",
    "T":"_t",
    "U":"_u",
    "V":"_v",
    "W":"_w",
    "X":"_x",
    "Y":"_y",
    "Z":"_z"}

# No action place holder
blank = ""

# For letters in the input
for char in user:
    # If the letter is capital, replace with snake_case
    if char in caps:
        blank += caps[char]
    # If the letter is lower case, no action taken
    else:
        blank += char

# Print snake_case output
print(blank)
