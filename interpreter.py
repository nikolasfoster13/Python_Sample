expr = input("Expression: ").strip()
variables = expr.split(" ")
if variables[1] == "+":
    value = float(float(variables[0])+float(variables[2]))
    rounded = round(value,2)
    print(rounded)
elif variables[1] == "-":
    value = float(float(variables[0])-float(variables[2]))
    rounded = round(value,2)
    print(rounded)
elif variables[1] == "/":
    value = float(float(variables[0])/float(variables[2]))
    rounded = round(value,2)
    print(rounded)
elif variables[1] == "*":
    value = float(float(variables[0])*float(variables[2]))
    rounded = round(value,2)
    print(rounded)
else:
    pass
