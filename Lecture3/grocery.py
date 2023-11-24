total = {}
while True:
    try:
        choice = input().upper()
        if choice in total:
            total[choice] += 1
        else:
            total[choice] = 1
    except EOFError:
        print()
        break

for key, value in sorted(total.items()):
    print(f"{value} {key}")
