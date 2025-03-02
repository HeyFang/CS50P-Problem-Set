amt = 50
coins = [5, 10, 25]

while amt > 0:
    print("Amount due:", amt)
    pay = int(input("Insert Coin: "))
    if pay not in coins:
        continue
    amt -= pay
    
print("Change Owed:", -amt)
