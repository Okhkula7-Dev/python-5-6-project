# Simple ATM System

balance = 5000
password = "1234"

print("Welcome to ATM")

user_password = input("Please enter your PIN: ")

if user_password == password:

    print("\nLogin Successful!")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Your balance is:", balance)

    elif choice == "2":
        amount = int(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance = balance - amount
            print("Please collect your money.")
            print("Remaining balance:", balance)

        else:
            print("Insufficient balance!")

    elif choice == "3":
        print("Thank you for using ATM!")

    else:
        print("Invalid option!")

else:
    print("Incorrect PIN!")