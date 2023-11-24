text = list(input("Input: ").strip())
output = []
for character in text:
    if character.lower() not in ["a","e","i","o","u"]:
        output.append(character)
print("Output: "+"".join(output))