import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if matches := re.search(r"^<iframe .*?src=\"(?:https?://)?(?:www\.)?youtube.com/embed/([^\"\?&/]+).*?></iframe>$", s, re.IGNORECASE):
        video_id = matches.group(1)
        return (f"https://youtu.be/{video_id}")
    else:
        pass

if __name__ == "__main__":
    main()
