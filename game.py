from random import randint
while True:
    try:
        level = int(input("Level: "))
        if level < 0:
            pass
        else:
            break
    except ValueError:
        pass
number = randint(1,level)
while True:
    try:
        guess = int(input("Guess: "))
        if guess == number:
            print("Just right!")
            break
        elif guess < 0:
            pass
        elif guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            pass
    except ValueError:
        pass

