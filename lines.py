import sys
file_type = sys.argv[1].split(".")
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(file_type) != 2 or file_type[1] != "py":
    sys.exit("Not a Python file")
try:
    line_cnt = 0
    with open(f"{sys.argv[1]}") as file:
        for line in file:
            if line.lstrip().startswith("#"):
                pass
            elif line.strip() == "":
                pass
            else:
                line_cnt += 1
    print(f"Lines = {line_cnt}")
except FileNotFoundError:
    sys.exit("File does not exist")


