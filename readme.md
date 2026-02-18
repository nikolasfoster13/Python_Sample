# File Extensions
extensions.py, is a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

- .gif
- .jpg
- .jpeg
- .png
- .pdf
- .txt
- .zip

If the file’s name ends with some other suffix or has no suffix at all, the program outputs application/octet-stream instead, which is a common default.