from random import randint

def main():
    level = get_level()
    count = 0
    score = 0
    while count != 10:
        chance = 3
        x, y = generate_integer(level)
        z = x + y
        for i in range(3):
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == z:
                    score += 1
                    count += 1
                    break
            except (ValueError, NameError):
                chance -= 1
                print("EEE")
                continue
            else:
                chance -= 1
                print("EEE")
        if chance == 0:
            print(f"{x} + {y} = {z}")
            count += 1
        else:
            continue
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 1 <= n <= 3:
                return n
        except:
            pass

def generate_integer(level):
    if level == 1:
        x = randint(0, 9)
        y = randint(0, 9)
    elif level == 2:
        x = randint(10, 99)
        y = randint(10, 99)
    elif level == 3:
        x = randint(100, 999)
        y = randint(100, 999)
    return x, y

if __name__ == "__main__":
    main()