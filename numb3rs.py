import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    try:
        # Create list of len 4 for input split on .
        split_list = ip.split(".")
        # Declare variables based on position in list, cast as int
        a = int(split_list[0])
        b = int(split_list[1])
        c = int(split_list[2])
        d = int(split_list[3])
        # Check that ints are in valid range, str version of list does not start with 0, and list length = 4
        if (0 <= a <= 255 and 0 <= b <= 255 and 0 <= c <= 255 and 0 <= d <= 255 and
        (not split_list[0].startswith("0") or a == 0) and (not split_list[1].startswith("0") or b == 0) and (not split_list[2].startswith("0") or c == 0) and (not split_list[3].startswith("0") or d == 0)
        and len(split_list) == 4):
            return True
        else:
            return False
    # If type error on input, return False
    except (TypeError, ValueError, IndexError):
        return False

if __name__ == "__main__":
    main()


