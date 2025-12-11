from random import randint
while True:
    try:
        # Prompt user for level
        level = int(input("Level: "))
        # If user provides nonpositive level number, reprompt
        if level <= 0:
            pass
        else:
            break
    # If user provides non-numeric level number, reprompt
    except ValueError:
        pass
# Generate random integer between 1 and prvodied level number
number = randint(1,level)
while True:
    try:
        # Prompt user for guess
        guess = int(input("Guess: "))
        # If user guess = number, print just right
        if guess == number:
            print("Just right!")
            break
        # If user provides non-positive guess, reprompt
        elif guess <= 0:
            pass
        # If user guess < number print too small
        elif guess < number:
            print("Too small!")
        # If user guess > number print too large
        elif guess > number:
            print("Too large!")
        else:
            pass
    # If user guess non-numeric, reprompt
    except ValueError:
        pass

