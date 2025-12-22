import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if matches := re.search(r"^([1-2]?[0-9])\:?([0-5][0-9])? (AM|PM) to ([1-2]?[0-9])\:?([0-5][0-9])? (AM|PM)$", s):
        start_h = matches.group(1).zfill(2)
        start_m = (matches.group(2) or "00").zfill(2)
        start_tod = matches.group(3)
        end_h = matches.group(4).zfill(2)
        end_m = (matches.group(5) or "00").zfill(2)
        end_tod = matches.group(6)

        if start_h == "12" and start_tod == "AM":
            start_time = f"00:{start_m}"
        elif start_h == "12" and start_tod == "PM":
            start_time = f"{start_h}:{start_m}"
        elif start_tod == "AM":
            start_time = f"{start_h}:{start_m}"
        elif start_tod == "PM":
            start_time = f"{str(int(start_h)+12)}:{start_m}"
        else:
            raise ValueError

        if end_h == "12" and end_tod == "AM":
            end_time = f"00:{end_m}"
        elif end_h == "12" and end_tod == "PM":
            end_time = f"{end_h}:{end_m}"
        elif end_tod == "AM":
            end_time = f"{end_h}:{end_m}"
        elif end_tod == "PM":
            end_time = f"{str(int(end_h)+12)}:{end_m}"
        else:
            raise ValueError

        hours = f"{start_time} to {end_time}"
        return hours
    else:
        raise ValueError
if __name__ == "__main__":
    main()
