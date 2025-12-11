from pyfiglet import Figlet
import sys
from random import choice

# If user runs program w/o declaring font
if len(sys.argv) == 1:
    figlet = Figlet()
    # Generate random font
    figlet.setFont(font = choice(figlet.getFonts()))
    # Prompt for input
    user = input("Input: ")
    # Print output in random font
    print("Output: \n",figlet.renderText(user))

# If user declares font and provides a valid font
elif (len(sys.argv) == 3) and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and (sys.argv[2] in Figlet().getFonts()):
    figlet = Figlet()
    figlet.setFont(font=sys.argv[2])
    # Prompt for input
    user = input("Input: ")
    # Print output in input font
    print("Output: \n",figlet.renderText(user))

# Else, exit program
else:
    print("Invalid usage")
    sys.exit


