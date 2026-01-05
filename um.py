import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    find = re.findall(r'\bum\b',s, re.IGNORECASE)
    count = len(find)
    return count

if __name__ == "__main__":
    main()
