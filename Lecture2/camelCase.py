def main():
    camelCase = input("camelCase: ").strip()
    convert(camelCase)
def convert(camelCase):
    for character in camelCase:
        if character.isupper():
            print("_"+character.lower(), end = "")
        else:
            print(character, end="")
if __name__ == "__main__":
    main()