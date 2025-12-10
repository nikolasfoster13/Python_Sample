# Defines 2 digit char to written months
months = {"January":"01",
    "February":"02",
    "March":"03",
    "April":"04",
    "May":"05",
    "June":"06",
    "July":"07",
    "August":"08",
    "September":"09",
    "October":"10",
    "November":"11",
    "December":"12"}

while True:
    # Prompts user for date
    user = input("Date: ").strip()
    # Splits input on space
    alpha_check = user.split(" ")
    # Splits input on comma
    comma_check = user.split(",")
    # Splits input on slash
    num_check = user.split("/")
    # Checks that if split on space, first str is alpha, the first str is a month, the input is comma separated after day, and the second str is a day <= 31
    if alpha_check[0].isalpha() == True and alpha_check[0] in months and comma_check.count() < 2 and int(alpha_check[1].rstrip(",")) <= 31:
        # Assigns the third str to year
        year = alpha_check[2]
        # Assigns the first str to month from dict
        month = months[alpha_check[0]]
        # Assigns the second str to day (remove , and pad with 0)
        day= alpha_check[1].rstrip(",").rjust(2,"0")
        # Print date YYYY-MM-DD
        print(f"{year}-{month}-{day}")
        break
    # Checks that if split on slash, first str is numeric, the first str is a month, and the second str is a day <= 31
    elif num_check[0].isnumeric() == True and int(num_check[0]) <= 12 and int(num_check[1]) <= 31:
        # Assigns the third str to year
        year = num_check[2]
        # Assigns the first str to month and pads 0
        month = num_check[0].rjust(2,"0")
        # Assigns the second str to day and pads 0
        day = num_check[1].rjust(2,"0")
        # Print date YYYY-MM-DD
        print(f"{year}-{month}-{day}")
        break
    # Reprompt if conditions are not met
    else:
        pass
