from validator_collection import validators

def main():
   print(validate(input("What's your email address? ")))


def validate(s):
    try:
        if validators.email(s) == None:
            return "Invalid"
        else:
            return "Valid"
    except ValueError:
        return "Invalid"
    except EmptyValueError:
        return "Invalid"

if __name__ == "__main__":
    main()


