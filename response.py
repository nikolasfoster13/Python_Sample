from validator_collection import validators, errors

#Prompt user for email and return valid or invalid
def main():
   print(validate(input("What's your email address? ")))


def validate(s):
    # Run email through validators.email
    try:
        # If None, return Invalid
        if validators.email(s) == None:
            return "Invalid"
        # Else, return Valid
        else:
            return "Valid"
    # Return errors as invalid
    except (ValueError, errors.EmptyValueError):
        return "Invalid"

if __name__ == "__main__":
    main()


