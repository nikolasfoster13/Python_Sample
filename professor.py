from random import randint

def main():
    # Generate level
    level = get_level()
    # Set list questions
    questions = []
    # Add 10 random questions to list questions
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        questions.append(f"{x} + {y} = ")
    # Set counter to 0
    _ = 0
    # Set incorrect counter to 0
    i = 0
    # Set score to 0
    score = 0
    # Loop 10 times for all 10 questions
    while _ <= 9:
        try:
            # Split question on +
            q = (questions[_]).split("+")
            # X = first int on split
            x = int(q[0])
            # Split remaining str on =
            y_var = (q[1]).split("=")
            # y = first int on split
            y = int(y_var[0])
            # Prompt user for answer
            answer = int(input(questions[_]))
            # If user answer = answer
            if answer == x+y:
                # Reset incorrect answer cnt
                i = 0
                # Add 1 to score
                score = score + 1
                # Add 1 to counter
                _ = _ + 1
            # If user provides incorrect answer
            else:
                # Print error
                print("EEE")
                # Add 1 to incorrect counter
                i = i + 1
                # If 3 incorrect
                if i == 3:
                    # Reset incorrect counter
                    i = 0
                    # Print correct answer
                    print(f"{questions[_]}{x+y}")
                    # Move to next question
                    _ = _ + 1
                else:
                    pass
        # If non-int answer
        except ValueError:
                # Print error
                print("EEE")
                # Add 1 to incorrect counter
                i = i + 1
                # If 3 incorrect
                if i == 3:
                    # Reset incorrect counter
                    i = 0
                    # Print correct answer
                    print(f"{questions[_]}{x+y}")
                    # Move to next question
                    _ = _ + 1
                else:
                    pass
    # Print final score
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
                x = randint(0,10)

                break
            # If level input = 2, generate 2 random variables between 10-99
            elif level == 2:
                x = randint(10,100)
                break
            # If level input = 3, generate 2 random variables between 100-999
            elif level == 3:
                x = randint(100,1000)
                break
            else:
                raise ValueError
        except ValueError:
            pass
    return x

if __name__ == "__main__":
    main()

