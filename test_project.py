import pytest
from project import word_generator, valid_guess, game_board

with open("words.txt") as f:
    # Create list of valid words, strip white space, capitalize word
    VALID_WORDS = [word.strip().upper() for word in f]

def test_word_generator():
    # word generator makes word
    assert word_generator().isalpha() == True
    # word is 5 characters
    assert len(word_generator()) == 5

def test_valid_guess():
    # valid guess returns true if user input is a valid 5 letter word
    assert valid_guess("feast") == True
    # valid guess returns false if user input is not 5 letters
    assert valid_guess("a") == False
    # valid guess returns false if user input is not a valid word
    assert valid_guess("aaaaa") == False

def test_game_board():
    # Game board function creates list
    assert game_board() == [
    "1._____",
    "2._____",
    "3._____",
    "4._____",
    "5._____"
    ]









