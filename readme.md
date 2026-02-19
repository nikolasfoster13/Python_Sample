# Frank, Ian, and Glen's Letters
FIGlet, named after Frank, Ian, and Glen’s letters, is a program from the early 1990s for making large letters out of ordinary text, a form of ASCII art.

Among the fonts supported by FIGlet are those at [figlet.org/examples.html].

FIGlet has since been ported to Python as a module called pyfiglet.

figlet.py is a program that:

* Expects zero or two command-line arguments. If zero, the user would like a random font. If two, the user would like to specify the font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
* Prompts the user for a string of text
* Outputs that text in the desired font

If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program exits via sys.exit and provides an error message.

