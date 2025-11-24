

def check_profit_loss(cp, sp):

    if sp > cp:
        return "Profit", sp - cp
    elif cp > sp:
        return "Loss", cp - sp
    else:
        return "No Profit No Loss", 0

def profit_loss_menu():
    print("Profit / Loss Calculator")
    cp = float(input("Enter Cost Price: "))
    sp = float(input("Enter Selling Price: "))

    status, amount = check_profit_loss(cp, sp)
    print(f"{status}: ₹{amount}")

check_profit_loss(10000, 25000)
profit_loss_menu()
