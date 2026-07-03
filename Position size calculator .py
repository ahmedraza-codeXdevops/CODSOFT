balance = float(input("Account Balance : "))
risk = float(input("Risk % : "))
entry = float(input("Entry Price : "))
sl = float(input("Stop Loss : "))

risk_amount = balance * risk / 100
risk_share = entry - sl

if risk_share > 0:
    qty = int(risk_amount / risk_share)
    print("Buy Quantity :", qty)
else:
    print("Invalid Stop Loss")