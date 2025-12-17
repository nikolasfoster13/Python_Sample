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
    menu = []
    with open(f"{sys.argv[1]}") as file:
        first_line = file.readline()
        headers = [h.strip() for h in first_line.rstrip().split(",")]
        for line in file:
            item,small,large = [x.strip() for x in line.rstrip().split(",")]
            menu.append([item, small, large])
    print(tabulate.tabulate(menu,headers = headers,tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")




