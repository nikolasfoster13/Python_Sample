from random import randint

def main():
    # Generate level
    level = get_level()
    # Set question counter to 1
    question = 1
    # Set score to 0
    score = 0
    # Set incorrect answer count to 0
    i = 0
    # Run loop 10 times
    while question <= 10:
        # Generate integers
        x,y = generate_integer(level)
        while True:
            try:
                # If user answer = the answer
                if int(input(f"{x} + {y} = ")) == (x + y):
                    # Reset incorrect answer count to 0
                    i = 0
                    # Add 1 to user score
                    score = score + 1
                    # Add 1 to the question counter
                    question = question + 1
                    break
                # If user answer != the answer
                else:
                    # Print error
                    print("EEE")
                    # Add 1 to the incorrect question count
                    i = i + 1
                    # If user answers incorrectly 3 times
                    if i == 3:
                        # Add 1 to the question counter
                        question = question + 1
                        # Reset incorrect answer count to 0
                        i = 0
                        # Provide user with correct answer
                        print(f"{x} + {y} = {x+y}")
                        break
                    else:
                        pass
            # If user provides non-numeric answer
            except ValueError:
                # Print error
                print("EEE")
                # Add 1 to the incorrect question count
                i = i + 1
                # If user answers incorrectly 3 times
                if i == 3:
                    # Add 1 to the question counter
                    question = question + 1
                    # Reset incorrect answer count to 0
                    i = 0
                    # Provide user with correct answer
                    print(f"{x} + {y} = {x+y}")
                    break
                else:
                    pass
    # Once 10 questions answered, provide correct answer score
    print(f"Score: {score}")

# Get level
def get_level():
    while True:
        try:
            # Prompt user for a level number
            level = int(input("Level: "))
            # Accept levels between 1-3, reprompt for different integers or input types
            if 1 <= level <= 3:
                return level
            else:
                pass
        except ValueError:
            pass

# Get integer
def generate_integer(level):
    while True:
        try:
            # If level input = 1, generate 2 random variables between 0-9
            if level == 1:
                x = randint(0,9)
                y = randint(0,9)
                break
            # If level input = 2, generate 2 random variables between 10-99
            elif level == 2:
                x = randint(10,99)
                y = randint(10,99)
                break
            # If level input = 3, generate 2 random variables between 100-999
            elif level == 3:
                x = randint(100,999)
                y = randint(100,999)
                break
            else:
                raise ValueError
        except ValueError:
            pass
    return x,y

if __name__ == "__main__":
    main()

