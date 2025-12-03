# Defines main function
def main():
    # Prompts user for sentence with :) or :(
    user_input = input(str("Convert your emotions to emojis! Provide a sentence using :( or :) and watch it convert to an emoji! "))
    # Converts user input to emojis
    user_input = convert(user_input)
    # Prints final output with emojis
    print(user_input)

# Defines function to convert text to emojis
def convert(user_input):
    # Replaces text with emojis for smiles & frowns
    user_input = user_input.replace(":)","🙂")
    user_input = user_input.replace(":(","🙁")
    return user_input

main()


