# Prompt user for expression
expr = input("Expression: ").strip()
# Split expression into 3 parts, x, operator, y
variables = expr.split(" ")
# If operator is + add x and y, print answer as rounded to 1 decimal
if variables[1] == "+":
    value = float(float(variables[0])+float(variables[2]))
    rounded = round(value,2)
    print(rounded)
# If operator is - subtract y from x, print answer as rounded to 1 decimal
elif variables[1] == "-":
    value = float(float(variables[0])-float(variables[2]))
    rounded = round(value,2)
    print(rounded)
# If operator is /, divide x by y, print answer as rounded to 1 decimal
elif variables[1] == "/":
    value = float(float(variables[0])/float(variables[2]))
    rounded = round(value,2)
    print(rounded)
# If operator is *, multiply x by y, print answer as rounded to 1 decimal
elif variables[1] == "*":
    value = float(float(variables[0])*float(variables[2]))
    rounded = round(value,2)
    print(rounded)
# If expression is not formatted properly, reprompt
else:
    pass
