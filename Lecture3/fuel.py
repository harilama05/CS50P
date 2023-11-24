while True:
    try:
        x, y = input("Fraction: ").split("/")
        x, y = int(x), int(y)
        if x>y:
            raise Exception
        elif y == 0:
            raise ZeroDivisionError
    except:
        pass
    else:
        break

frac = (x/y)*100
if frac<=1:
    print("E")
elif frac>=99:
    print("F")
else:
    print(f"{frac:.0f}%")