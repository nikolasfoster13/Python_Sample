import sys
import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
file_name,file_type = sys.argv[1].split(".")
if file_type != "csv":
    sys.exit("Invalid file type")
try:
    headers = []
    menu = []
    with open(f"{sys.argv[1]}") as file:
        for line in file:
            item,small,large = line.rstrip().split(",")
            items = {"item":item, "small":small, "large":large}
            menu.append(items)
    print(tabulate.tabulate(menu,tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")




