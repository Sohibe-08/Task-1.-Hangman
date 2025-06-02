stock = {"AAPL" : 180, "TSLA" : 250}
x = input("Enter the stock name: ").upper()
y = int(input("Enter the quantity: "))
if x in stock:
    total = y * stock[x]
    print("Total:", total)
else:
    print("Wrong name")