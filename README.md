# WORDLE
## Created By:
Nick Foster\
GitHub | edX: nikolasfoster13\
Kuna, ID USA\
8 January, 2026
## Description:
Project.py is a python clone of the popular word puzzle game "Wordle" by NYT Games. Project.py generates a random 5 letter word from the a text file containing valid "Wordle" words. The user is then given 5 chances to guess the 5 letter word. If the user inputs a word less than 5 characters and/or their guess is not in the valid list, they are reprompted.

With each guess:
- If the letter is correct and in the correct location, the letter will be changed to the color green on both the game board and the available letter board.
- If the letter is correct, but not in the correct location, the letter will be changed to yellow on both the game board and the available letter board.
- If the letter is not correct, the letter will be white on the game board and dimmed on the available letter board.

If the user successfully guesses the word within the 5 guesses, they will be congratulated and prompted to replay. If the user does not successfully guess, the program will provide a "You Lose" dialogue and inform the user of the correct word before prompting to play again.
## Requirements:
In order to run project.py, you will need the following required files and packages:
- <ins>**words.txt:**</ins> This is a text document that contains a list of approximately 13k valid words sourced from the NY Times website. This list can be found on GitHub from user cfreshman at https://gist.github.com/cfreshman/a03ef2cba789d8cf00c08f767e0fad7bwords.
- <ins>**colorama:**</ins> Colorama must be installed via pip installer. The colorama package makes ANSI escape character sequences (for producing colored terminal text and cursor positioning). This package is essential in the color coding required by the program. Official documentation can be found at https://pypi.org/project/colorama/#description.

Additional built in packages required to run project.py include:
- <ins>**random:**</ins> The random module is a built in library to perform pseudo-random operations. Official documentation can be found at https://docs.python.org/3/library/random.html.
- <ins>**os:**</ins> The os module is a built in library that allows your script to interact with your system's built in operating system. Official documentation can be found at https://docs.python.org/3/library/os.html.
- <ins>**sys:**</ins> The sys module is a built in library that allows your script to interact directly with the Python interpreter. Official documentation can be found at https://docs.python.org/3/library/sys.html.

## Video Demonstration:
Video demonstration of the program can be found at the following link https://youtu.be/n7CD7V4rKmw.

## Code Breakdown:
Project.py utilizes the following functions to run the main program. Expand this section to see a breakdown of each of the implemented functions.
<details>
<summary>Detailed Code Breakdown</summary>

- <ins>**word_generator():**</ins> A simple function that calls from a list of valid Wordle words and selects a random word from that list.
```python
def word_generator():
    return random.choice(VALID_WORDS)
```
- <ins>**valid_guess():**</ins> Ensures that the user provided guess exists in the valid Wordle word list. This helps ensure that user input is a 5 character valid word.
```python
def valid_guess(w):
    return w.upper() in VALID_WORDS
```
- <ins>**game_board():**</ins> Creates a list that makes a structured "game board" for the user. This board will be edited with each user guess.
```python
def game_board():
    return [
    "1._____",
    "2._____",
    "3._____",
    "4._____",
    "5._____"
    ]
```
- <ins>**update_board():**</ins> Replaces the underscores on the game board with the user's guess for each level of the game.
```python
def update_board(board, level, guess):
    index = level - 1
    board[index] = f"{level}.{guess}"
```

- <ins>**print_board():**</ins> Prints the game board. If board is unedited, it'll show in the same format as the function game_board(). If it has been edited, lines will be populated with user guesses.
```python
def print_board(board):
    for line in board:
        print(line)
```
- <ins>**create_letter_board():**</ins> Creates a variable letters that is a string of all 26 english characters. These characters are set to a text color of white by default.
```python
def create_letter_board():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return {letter: Fore.WHITE + letter + Style.RESET_ALL for letter in letters}
```
- <ins>**print_letter_board():**</ins> Creates a list of the characters created in the create_letter_board() function. Then prints the list as two sets of 13 for visual aesthetic.
```python
def print_letter_board(letter_board):
    letters = list(letter_board.values())
    print(", ".join(letters[:13]))
    print(", ".join(letters[13:]))
```
- <ins>**update_letter_board():**</ins> Identifies if the letter in a guess is in the word. If the letter from the user string is in the correct location and is the correct letter, the letter on the letter board will be updated to green to represent a correct guess. If the letter from the user string is the correct letter but is not in the correct location, the letter on the letter board will be updated to yellow to represent a "close" guess. If the letter from the user string is not in the word, the letter will be dimmed to represent an incorrect guess.
```python
def update_letter_board(letter_board, guess, word):
    for i, ch in enumerate(guess):
        if ch == word[i]:
            letter_board[ch] = Fore.GREEN + ch + Style.RESET_ALL
        elif ch in word:
            if Fore.GREEN not in letter_board[ch]:
                letter_board[ch] = Fore.YELLOW + ch + Style.RESET_ALL
        else:
            if (Fore.GREEN not in letter_board[ch] and Fore.YELLOW not in letter_board[ch]):
                letter_board[ch] = Style.DIM + Fore.WHITE + ch + Style.RESET_ALL
```
- <ins>**clear_screen():**</ins> Clears the terminal window to prevent overflow from multiple prompts.
```python
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
```
- <ins>**colored_guess():**</ins> Similar to the update_letter_board() function, this function will colorcode a user's guessed letters on the main game board. If the letter is correct and in the correct position, the font color will be green. If the letter is correct but in the wrong position, the font color will be yellow.
If the letter is not correct, the color will remain white.
```python
def color_guess(guess, word):
    guess = guess.upper()
    word = word.upper()
    colored = [""] * 5
    word_letter_counts = {}
    for ch in word:
        word_letter_counts[ch] = word_letter_counts.get(ch,0)+1
    matched_counts = {ch: 0 for ch in word_letter_counts}
    for i, ch in enumerate(guess):
        if ch == word[i]:
            colored[i] = Fore.GREEN + ch + Style.RESET_ALL
            matched_counts[ch] += 1
    for i, ch in enumerate(guess):
        if colored[i]:
            continue
        if ch in word_letter_counts and matched_counts[ch] < word_letter_counts[ch]:
            colored[i] = Fore.YELLOW + ch + Style.RESET_ALL
            matched_counts[ch] += 1
        else:
            colored[i] = Fore.WHITE + ch + Style.RESET_ALL
    return "".join(colored)
```
- <ins>**menu():**</ins> This function prints a 4 line menu that displays options for a user upon start of the program.
```python
def menu():
    print("WORDLE!")
    print("1. Play")
    print("2. How to Play")
    print("3. Quit")
```
- <ins>**game():**</ins> This is the main logic function of the game. The game will generate a random word from the valid Wordle list. The game will then initialize and print the game board and letter board and set the first guess to 1.


    While the guess number is less than 5, the game will prompt user for a guess. If the user's guess is not a valid word, it will produce an error message and reprompt the user. If the user's guess is valid, the screen will update with guess now populated on the board with color coding and the guessed letters color coded on the letter board.

    If the user's guess was not the word, the game will move to guess 2. This process will repeat for all 5 guesses.

    If the user successfully guesses the word within 5 guesses, the program will produce a congratulatory message and prompt the user to replay.

    If the user fails to guess the word within 5 guesses, the program will produce an unsatisfactory message and prompt the user to replay.
```python
def game():
    word = word_generator().upper()
    board = game_board()
    print_board(board)
    letter_board = create_letter_board()
    guess_num = 1
    while guess_num <= 5:
        guess = input("Guess: ").upper()
        while len(guess) !=5 or not valid_guess(guess):
            print("Your guess must be a 5 letter, valid English word!")
            guess = input("Guess: ").upper()
        clear_screen()
        colored = color_guess(guess, word)
        update_board(board, guess_num, colored)
        update_letter_board(letter_board, guess, word)
        print_board(board)
        print_letter_board(letter_board)
        guess_num = guess_num + 1
        if guess == word:
            print("Congratulations! You guessed the word")
            play_again = input("\nPlay again? (Y/N): ").upper()
            if play_again == "Y":
                clear_screen()
                game()
                return
            else:
                return
    if guess_num == 6:
        clear_screen()
        print_board(board)
        print(f"Sorry, you lose...")
        print(f'The correct word was "{word}"!')
    play_again = input("\nPlay again? (Y/N): ").upper()
    if play_again == "Y":
        clear_screen()
        game()
        return
    else:
        return
```
- <ins>**how_to_play():**</ins> This function prints instructions on how to play the game.
```python
def how_to_play():
    print("HOW TO PLAY")
    print("Guess the 5-letter word in 5 tries.")
    print("Green = correct letter, correct spot.")
    print("Yellow = correct letter, wrong spot.")
    print("Gray = letter not in the word.")
    input("\nPress Enter to return to the menu..")
```
- <ins>**main():**</ins> This function runs the entirety of the game program.

    The program begins by clearing the terminal window and displaying the main menu via the menu() funciton. The user is then prompted to input their selection.

    If the user inputs 1, the main game function will run via the game() function. If the user inputs 2, the instruction menu via the how_to_play() function. If the user inputs 3, the game will exit and display a goodbye message. All other inputs are considered invalid and will reprompt the user.
```python
def main():
    while True:
        clear_screen()
        menu()
        choice = input("Select an option: ").strip()
        if choice == "1":
            clear_screen()
            game()
        elif choice == "2":
            clear_screen()
            how_to_play()
        elif choice == "3":
            sys.exit("Thanks for playing!")
        else:
            print("Invalid choice. Try again.")
            input("Press Enter...")
```
</details>

## Connect with me!
[LinkedIn](https://www.linkedin.com/in/nikolas-foster-4933b517a)

