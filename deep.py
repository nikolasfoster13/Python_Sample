answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

if answer.lower().strip() == "42":
    print("Yes")
elif answer.lower().strip() == "fourty-two":
    print("Yes")
elif answer.lower().strip() == "fourty two":
    print("Yes")
else:
    print("No")
