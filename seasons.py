from datetime import date, datetime
import sys
import inflect

def main():
    # Prompt user for birthday, strip white space
    birthday = input("What's your birthday? (YYYY-MM-DD) ").strip()
    # Find age in minutes
    minutes = date_diff(birthday)
    p = inflect.engine()
    # Print age in minutes as words
    print(num_to_word(minutes).capitalize(),p.plural_noun("minute",minutes))

def date_diff(bd):
    try:
        # Convert provided string to date
        d1 = datetime.strptime(bd, "%Y-%m-%d").date()
        # Find today's date
        d2 = date.today()
        # Calculate minutes difference
        minutes = (d2 - d1).days * 24 * 60
        return minutes
    except ValueError:
        # If invalid date format, exit with error message
        sys.exit("Invalid date format")

def num_to_word(minutes):
    p = inflect.engine()
    # Convert minutes to words and remove "and"
    words = p.number_to_words(minutes, andword="")
    return words


if __name__ == "__main__":
    main()
