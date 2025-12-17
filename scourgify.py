import sys
import csv
try:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    b_file_name,b_file_type = sys.argv[1].split(".")
    a_file_name,a_file_type = sys.argv[2].split(".")
    if b_file_type != "csv" or a_file_type != "csv":
        sys.exit("Invalid file type")

    students = []
    with open(f"{sys.argv[1]}") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({"name":row["name"], "house":row["house"]})

    with open(f"{sys.argv[2]}","w") as file:
        file.write("first,last,house\n")

    for student in students:
        last, first = [part.strip() for part in student["name"].split(",")]
        house = student["house"]
        with open(f"{sys.argv[2]}","a") as file:
            file.write(f"{first},{last},{house}\n")
except FileNotFoundError:
    sys.exit("File does not exist")


