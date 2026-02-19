# Guessing Game
game.py is a program that:
* Prompts the user for a level (n). If the user does not input a positive integer, the program will prompt again.
* Randomly generates an integer between 1 and n.
* Prompts the user to guess that integer. If the guess is not a positive integer, the program will prompt again.
    * If the guess is smaller than the integer, the program will output "Too small!" and reprompt the user.
    * If the guess it larger than the integer, the program will output "Too large!" and reprompt the user.
    * If the guess is the same as the integer, the program will output "Just right!" and exit.