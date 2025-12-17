import sys
from PIL import Image, ImageOps
try:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    b_file_name,b_file_type = sys.argv[1].split(".")
    a_file_name,a_file_type = sys.argv[2].split(".")
    allowed_types = {"jpg","jpeg","png"}
    if b_file_type.lower() not in allowed_types or a_file_type.lower() not in allowed_types:
        sys.exit("Invalid file type")
    if b_file_type.lower() != a_file_type.lower():
        sys.exit("Input and output file types do not match")
    else:
        picture = Image.open(f"{sys.argv[1]}")
        shirt = Image.open("shirt.png")
        picture = ImageOps.fit(picture, size = shirt.size)
        picture.paste(shirt,shirt)
        picture.save(sys.argv[2])
except FileNotFoundError:
    sys.exit("File does not exist")



