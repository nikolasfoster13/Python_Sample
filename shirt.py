import sys
from PIL import Image, ImageOps
try:
    # Verify the length of CLA is exactly 3
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # Split CLA file names by name and type
    b_file_name,b_file_type = sys.argv[1].split(".")
    a_file_name,a_file_type = sys.argv[2].split(".")
    # Define allowed file types
    allowed_types = {"jpg","jpeg","png"}

    # Check that file types provided are allowed
    if b_file_type.lower() not in allowed_types or a_file_type.lower() not in allowed_types:
        sys.exit("Invalid file type")

    # Check that input and output file types match
    if b_file_type.lower() != a_file_type.lower():
        sys.exit("Input and output file types do not match")
    else:
        # Open input file
        picture = Image.open(f"{sys.argv[1]}")
        # Open shirt file
        shirt = Image.open("shirt.png")
        # Fit input file to match size of shirt file
        picture = ImageOps.fit(picture, size = shirt.size)
        # Paste shirt on input picture
        picture.paste(shirt,shirt)
        # Save new picture with output name provided
        picture.save(sys.argv[2])

# If input file not found, exit
except FileNotFoundError:
    sys.exit("File does not exist")



