counter = {}
x = 0
while True:
    try:
        item = input().strip().upper()
    except EOFError:
        break
    else:
        counter[item] = counter.get(item,0)+1

print("")
for item in sorted(counter):
    print(f"{counter[item]} {item}")
