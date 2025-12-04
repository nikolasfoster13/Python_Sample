file = input("File name: ")

if file.strip().lower().endswith(".gif"):
    print("image/gif")
elif file.strip().lower().endswith(".jpg") or file.strip().lower().endswith(".jpeg"):
    print("image/jpeg")
elif file.strip().lower().endswith(".png"):
    print("image/png")
elif file.strip().lower().endswith(".pdf"):
    print("application/pdf")
elif file.strip().lower().endswith(".txt"):
    print("text/plain")
elif file.strip().lower().endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")

