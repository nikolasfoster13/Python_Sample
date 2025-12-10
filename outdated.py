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
    user = input("Date: ")
    alpha_check = user.split(" ")
    num_check = user.split("/")
    if alpha_check[0].isalpha() == True and alpha_check[0] in months and int(alpha_check[1].rstrip(",")) <= 31:
        year = alpha_check[2]
        month = months[alpha_check[0]]
        day= alpha_check[1].rstrip(",").rjust(2,"0")
        print(f"{year}-{month}-{day}")
        break
    elif num_check[0].isnumeric() == True and int(num_check[0]) <= 12 and int(num_check[1]) <= 31:
        year = num_check[2]
        month = num_check[0].rjust(2,"0")
        day = num_check[1].rjust(2,"0")
        print(f"{year}-{month}-{day}")
        break
    else:
        pass
