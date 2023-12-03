from random import randint
check = False
while not check:
    level = input("Level: ")
    check = level.isnumeric()

rand = randint(1,int(level))
while True:
    try:
        guess = int(input('Guess: '))
        if guess > rand:
            print("Too large!")
        elif guess < rand:
            print("Too small!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass

    