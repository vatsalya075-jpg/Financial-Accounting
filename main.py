
import interest
import loan
import profitloss

def main():
    while True:
        print("Finance & Accounting Program")
        print("1. Simple Interest")
        print("2. Loan EMI")
        print("3. Profit / Loss")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            interest.interest_menu()
        elif choice == "2":
            loan.loan_menu()
        elif choice == "3":
            profitloss.profit_loss_menu()
        elif choice == "4":
            print("Exiting Program...")
            break
        else:
            print("Invalid Choice! Try again.\n")

main()
