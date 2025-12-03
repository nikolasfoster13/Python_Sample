greeting = input("Please provide a greeting: ")

if greeting.lower().strip().startswith("hello") == True:
    print("$0")
elif greeting.lower().strip().startswith("h") == True:
    print("$20")
else:
    print("$100")

