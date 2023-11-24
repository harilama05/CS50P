def main():
    plate = list(input("Plate: "))
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
def seperate(s):
    for i in range(len(s)):
        if s[i].isnumeric():
            letters = s[:i]
            numbers = s[i:]
            break
        else:
            letters = s
            numbers = []
    return letters, numbers
def is_valid(s):
    letters, numbers = seperate(s)
    check_number = []
    for z in range(len(numbers)):
        if numbers[0] == "0":
            return False
        elif numbers[z].isnumeric():
            check_number.append(numbers[z])
    if 1<len(s)<7 and len(letters) >1:
        if len(check_number) == len(numbers):  
            return True 
    else: return False
if __name__ == "__main__":
    main()