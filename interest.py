def calculate_simple_interest(p, r, t):

    si = (p * r * t) / 100
    return si

def interest_menu():
    print("Simple Interest Calculator")
    p = float(input("Enter Principal Amount: "))
    r = float(input("Enter Rate of Interest: "))
    t = float(input("Enter Time (in years): "))

    si = calculate_simple_interest(p, r, t)
    print(f"Simple Interest = {si}")

calculate_simple_interest(5,4,6)
interest_menu()
