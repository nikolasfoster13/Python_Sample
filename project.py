from colorama import Fore, Style
import random
import os
import sys

# Open the text file containing a list of valid WORDLE words
with open("words.txt") as f:
    # Create list of valid words, strip white space, capitalize word
    VALID_WORDS = [word.strip().upper() for word in f]

def main():
    while True:
        # Start with clear screen
        clear_screen()
        # Present menu
        menu()
        # Prompt user for menu input
        choice = input("Select an option: ").strip()
        # If user selects game, clear screen and launch game funciton
        if choice == "1":
            clear_screen()
            game()
        # If user selects "How to", clear screen and launch how to play function
        elif choice == "2":
            clear_screen()
            how_to_play()
        # If user selects "quit", exit program
        elif choice == "3":
            sys.exit("Thanks for playing!")
        # All other inputs are invalid, reprompt user
        else:
            print("Invalid choice. Try again.")
            input("Press Enter...")
            
# Select a random word from the word list
def word_generator():
    return random.choice(VALID_WORDS)

# Confirm that the user guess is in the valid word list
def valid_guess(w):
    return w.upper() in VALID_WORDS

# Create the game board
def game_board():
    return [
    "1._____",
    "2._____",
    "3._____",
    "4._____",
    "5._____"
    ]

# Add user guess to line number
def update_board(board, level, guess):
    index = level - 1
    board[index] = f"{level}.{guess}"

# Print the board
def print_board(board):
    for line in board:
        print(line)

# Create the letter board
def create_letter_board():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Set letters to white and reset format after each letter
    return {letter: Fore.WHITE + letter + Style.RESET_ALL for letter in letters}

# Print the letter board in a readable format
def print_letter_board(letter_board):
    letters = list(letter_board.values())
    # Print letters in bunches of 13 sep by , for visual aesthetic
    print(", ".join(letters[:13]))
    print(", ".join(letters[13:]))

# Color code the letter board with user guesses
def update_letter_board(letter_board, guess, word):
    for i, ch in enumerate(guess):
        # If guess is accurate, make letter green
        if ch == word[i]:
            letter_board[ch] = Fore.GREEN + ch + Style.RESET_ALL
        # If guess is not green, check if letter is in word, change letter to yellow
        elif ch in word:
            if Fore.GREEN not in letter_board[ch]:
                letter_board[ch] = Fore.YELLOW + ch + Style.RESET_ALL
        # If guess is not yellow or green, change letter to DIM to represent a wrong guess
        else:
            if (Fore.GREEN not in letter_board[ch] and Fore.YELLOW not in letter_board[ch]):
                letter_board[ch] = Style.DIM + Fore.WHITE + ch + Style.RESET_ALL

# Clears terminal window
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# Color code the lines of the game board with user guess
def color_guess(guess, word):
    guess = guess.upper()
    word = word.upper()
    colored = [""] * 5
    word_letter_counts = {}
    for ch in word:
        word_letter_counts[ch] = word_letter_counts.get(ch,0)+1
    matched_counts = {ch: 0 for ch in word_letter_counts}
    # If guess is accurate, make letter green
    for i, ch in enumerate(guess):
        if ch == word[i]:
            colored[i] = Fore.GREEN + ch + Style.RESET_ALL
            matched_counts[ch] += 1
    # If guess is in the word, make letter yellow
    for i, ch in enumerate(guess):
        if colored[i]:
            continue
        if ch in word_letter_counts and matched_counts[ch] < word_letter_counts[ch]:
            colored[i] = Fore.YELLOW + ch + Style.RESET_ALL
            matched_counts[ch] += 1
        # If guess is not in word, make letter white
        else:
            colored[i] = Fore.WHITE + ch + Style.RESET_ALL
    return "".join(colored)

# Creates main menu visual
def menu():
    print("WORDLE!")
    print("1. Play")
    print("2. How to Play")
    print("3. Quit")

# Playable game funciton
def game():
    # Generate random word
    word = word_generator().upper()
    # Generate the game board
    board = game_board()
    # Print the game board
    print_board(board)
    letter_board = create_letter_board()
    # Set guess number = 1
    guess_num = 1
    # Until user hits 5th guess
    while guess_num <= 5:
        # prompt user for guess
        guess = input("Guess: ").upper()
        while len(guess) !=5 or not valid_guess(guess):
            print("Your guess must be a 5 letter, valid English word!")
            guess = input("Guess: ").upper()
        # Clear the screen
        clear_screen()
        # Color code guess
        colored = color_guess(guess, word)
        # Update the game board with their guess
        update_board(board, guess_num, colored)
        update_letter_board(letter_board, guess, word)
        # Reprint the board
        print_board(board)
        print_letter_board(letter_board)
        # Update the guess number in loop
        guess_num = guess_num + 1
        if guess == word:
            # If user guesses correctly, congratulate user and prompt for play again
            print("Congratulations! You guessed the word")
            play_again = input("\nPlay again? (Y/N): ").upper()
            if play_again == "Y":
                clear_screen()
                game()
                return
            else:
                return
    if guess_num == 6:
        # If user doesn't get it in 5 guesses, give failure message, give correct word, and prompt for play again
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

# Displays game rules
def how_to_play():
    print("HOW TO PLAY")
    print("Guess the 5-letter word in 5 tries.")
    print("Green = correct letter, correct spot.")
    print("Yellow = correct letter, wrong spot.")
    print("Gray = letter not in the word.")
    input("\nPress Enter to return to the menu..")

if __name__ == "__main__":
    main()
