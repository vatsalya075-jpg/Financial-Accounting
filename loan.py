def calculate_emi(p, r, n):
    monthly_r = r / (12 * 100)

    emi = p * monthly_r * (1 + monthly_r)**n / ((1 + monthly_r)**n - 1)
    return emi

def loan_menu():
    print("Loan EMI Calculator")
    p = float(input("Enter Loan Amount: "))
    r = float(input("Enter Annual Interest Rate (%): "))
    n = int(input("Enter Loan Duration (months): "))

    emi = calculate_emi(p, r, n)
    print(f"Your Monthly EMI = {emi:.2f}")


loan_menu()
calculate_emi(200000, 8, 9)

