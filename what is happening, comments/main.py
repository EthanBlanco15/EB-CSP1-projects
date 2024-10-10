#Ethan Blanco, ProficiencyTest: What is happening?
#To clarify, this piece of code does NOT belong to me.

"""
This program is about creating a bank account, depositing, withdrawing, having an initial amount of money, checking balance and exiting the program.

"""

class BankAccount: #This is the definition for our bank account that this program uses.
    def __init__(self, account_number, balance=0):
        self.account_number = account_number #This creates our variables for the functions below.
        self.balance = balance

    def deposit(self, amount): #This is our deposit function, from the users input, it adds a select amount of money into our account.
        if amount > 0:
            self.balance += amount
            return True #If the amount the user inputs is sufficient, it will print out how much it adds to our balance.
        return False #If the amount the user inputs is inefficient, it will not work and will return to the previous section.

    def withdraw(self, amount): #This is our withdraw function, from the users input, it subtracts a select amount of money from our account.
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True#If the amount the user inputs is sufficient, it will print out how much it subtracted to our balance.
        return False#If the amount the user inputs is inefficient, it will not work and will return to the previous section.

    def get_balance(self): #When we use either the withdraw, deposit, create account functions, this returns us to the previous point.
        return self.balance

def create_account():
    account_number = input("Enter account number: ") #This creates our account and number.
    initial_balance = float(input("Enter initial balance: ")) #This creates our initial balance, anything the user inputs will be our account balance.
    return BankAccount(account_number, initial_balance) #This returns the function back to a main point.
"""
This function below is our select choices for what we will use
Option 1 is to create an account.
Option 2 is to deposit with our initial balance.
Option 3 is to withdraw with our initial balance.
Option 4 is to check our initial balance.
Option 5 is to exit and quit the program.
"""
def main():
    accounts = {}
    while True:
        print("\n1. Create Account") 
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ") #The function below is what the program does when the user inputs a printed choice.
        
        if choice == '1':
            account = create_account()
            accounts[account.account_number] = account
            print(f"Account {account.account_number} created successfully!") #This function is what will happen after we create our account.
        
        elif choice in ['2', '3', '4']:
            account_number = input("Enter account number: ") #This asks for our specific account number so that we can access the same bank account.
            if account_number in accounts:
                account = accounts[account_number]
                if choice == '2':
                    amount = float(input("Enter deposit amount: "))
                    if account.deposit(amount):
                        print(f"Deposited ${amount:.2f} successfully!") #This is our printed out statement after a successful deposit.
                    else:
                        print("Invalid deposit amount.") #This is what prints out after an error or invalid syntax.
                elif choice == '3':
                    amount = float(input("Enter withdrawal amount: ")) #This is our printed out statement after a successful withdrawl.
                    if account.withdraw(amount):
                        print(f"Withdrawn ${amount:.2f} successfully!")
                    else:
                        print("Invalid withdrawal amount or insufficient funds.") #This print out statement is what happens if we enter a string instead or are depositing/withdrawing more or less our balance is.
                else:
                    print(f"Current balance: ${account.get_balance():.2f}") #This helps the user see what is left in our account.
            else:
                print("Account not found.") #This is the possibility if you input the wrong bank account number or haven't created an account yet.
        
        elif choice == '5':
            print("Thank you for using our banking system. Goodbye!") #This is our 5th option to quit the program.
            break
        
        else:
            print("Invalid choice. Please try again.") #This is when the user enters an invalid syntax.

if __name__ == "__main__":
    main() #This sets us back to the beginning after quitting.