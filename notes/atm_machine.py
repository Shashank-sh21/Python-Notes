def atm_machine():
    """Simulates a basic ATM machine with balance inquiry, withdrawal, and deposit functionalities."""

    balance = 1000  # Initial balance

    while True:
        print("\nWelcome to the ATM Machine!")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Your balance is:", balance)
        elif choice == 2:
            withdraw_amount = int(input("Enter the amount to withdraw: "))
            if withdraw_amount <= balance:
                balance -= withdraw_amount
                print("Withdrawal successful. Your new balance is:", balance)
            else:
                print("Insufficient balance.")
        elif choice == 3:
            deposit_amount = int(input("Enter the amount to deposit: "))
            balance += deposit_amount
            print("Deposit successful. Your new balance is:", balance)
        elif choice == 4:
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    atm_machine()
