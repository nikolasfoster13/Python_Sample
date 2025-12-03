answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

if int(answer) == 42 or answer.lower() == "fourty-two" or answer.lower() == "fourty two":
    print("Yes")
else:
    print("No")
