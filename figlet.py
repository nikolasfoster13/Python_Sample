from pyfiglet import Figlet
from sys import argv, exit
from random import choice

# If user runs program w/o declaring font
if len(argv) == 1:
    figlet = Figlet()
    # Generate random font
    figlet.setFont(font = choice(figlet.getFonts()))
    # Prompt for input
    user = input("Input: ")
    # Print output in random font
    print("Output: \n",figlet.renderText(user))

# If user declares font and provides a valid font
elif (len(argv) == 3) and (argv[1] == "-f" or argv[1] == "--font") and (argv[2] in Figlet().getFonts()):
    figlet = Figlet()
    figlet.setFont(font=argv[2])
    # Prompt for input
    user = input("Input: ")
    # Print output in input font
    print("Output: \n",figlet.renderText(user))

# Else, exit program
else:
    print("Invalid usage")
    exit


