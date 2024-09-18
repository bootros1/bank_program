print("Welcome to BB Bank!")

# Initialize the balance
balance = 0.00

# Function to display menu
def display_menu():
    print("--- Banking Program ---")
    print("1. Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

# Function to view balance
def view_balance():
    print(f"Your balance is ${balance}")

# Function to deposit money
def deposit(balance):
    amount= float(input("Enter your deposit amount: "))
    if amount > 0:
        balance += amount
        print(f"Deposit was successful. New balance ${balance}")
    else:
        print("Invalid amount. Enter a positive value.")
    return balance

# Function to withdraw money
def withdraw(balance):
    amount = float(input("Enter your withdrawal amount: "))
    if 0 < amount <= balance:
        balance -= amount
        print(f"Withdrawal successful. New balance ${balance}")
    else:
        print("Insufficient funds")
    return balance

# Main function to handle the banking program
def main():
    global balance
    while True:
        display_menu()
        option = input("Please choose an option: (1-4) ")
        if option == "1":
            view_balance()
        elif option == "2":
            balance = deposit(balance)
        elif option == "3":
            balance = withdraw(balance)
        elif option == "4":
            break
        else:
            print("Invalid option. Please choose a valid option.")

    print("Thank you for using our service. See you soon!")

# Run the main function
if __name__ == "__main__":
    main()