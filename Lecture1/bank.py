user = input("Greeting: ").lower().strip()
if user[0:5] == "hello":
    print("$0")
elif user[0] == "h":
    print("$20")
else: 
    print("$100")