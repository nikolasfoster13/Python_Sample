def main():
    # User provides time of day
    tod = input("What time is it?: ").lower()

    # Calls converted time
    ctod = convert(tod)

    # If time between 7 & 8 am, then breakfast time
    if 7 <= ctod <= 8:
        print("breakfast time")

    # If time between 12 & 1 pm, then lunch time
    elif 12 <= ctod <= 13:
        print("lunch time")

    #if time between 6 & 7 pm, then dinner time
    elif 18 <= ctod <= 19:
        print("dinner time")

def convert(tod):
    # Splits am/pm from time is user provided
    time, am_pm = tod.strip().split(" ")

    # If user provides between 12:00 am - 12:59 am, return hours as 0
    if am_pm == "am" and time.startswith("12"):
        hours, minutes = time.split(":")
        chours = float(hours) - 12
        cminutes = float(minutes)/60

    # If user provides between 1:00 am - 12:59 pm, separate hours and minutes
    elif (am_pm == "am") or (am_pm == "pm" and time.startswith("12")):
        hours, minutes = time.split(":")
        chours = float(hours)
        cminutes = float(minutes)/60

    # if user provides between 1:00 pm - 11:59 pm, separate hours add 12 and minutes
    elif am_pm == "pm":
        hours, minutes = time.split(":")
        chours = float(hours) + 12
        cminutes = float(minutes)/60

    # If user provides 24-hour format, separate hours and minutes
    else:
        hours,minutes = tod.split(":")
        chours = float(hours)
        cminutes = float(minutes)/60

    # Adds converted hours and minutes to get a float output for comparrison
    ctod = chours + cminutes
    return ctod

if __name__ == "__main__":
    main()
