amount_due = 50
while True:
    print("Amount Due:",amount_due)
    insert_coin = int(input("Insert Coin: "))
    if insert_coin in [5,10,25]:
        amount_due -= insert_coin
        if amount_due <= 0:
            print(f"Change Owed: {amount_due}".replace("-", ""))
            break
    else: 
        continue
    