class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return amount
        else:
            return "Insufficient funds"

#Coded by Shreyas D Y
atm = ATM(1000)
print("Welcome to the ATM!")
while True:
    print("Please select an option:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    option = input()
    if option == "1":
        print("Your balance is:", atm.check_balance())
    elif option == "2":
        amount = int(input("Enter the amount to deposit: "))
        print("Your new balance is:", atm.deposit(amount))
    elif option == "3":
        amount = int(input("Enter the amount to withdraw: "))
        print("You withdrew:", atm.withdraw(amount))
    elif option == "4":
        print("Thank you for using the ATM.")
        break
    else:
        print("Invalid option. Please try again.")
