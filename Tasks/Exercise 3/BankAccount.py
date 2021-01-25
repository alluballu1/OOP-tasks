# main function?
import bank_class


def main():
    # get the starting balance
    start_bal = float(input("Enter the starting balance: "))
    owner = input("Enter the owner: ")

    # create a BankAccount object
    savings = bank_class.BankAccount(start_bal, owner)
    another_ba = ...

    # Display the balance
    print("Balance is: ", format(savings.get_balance(), ",.2f"), sep="")

    # Get the amount to deposit
    amount = float(input("Enter the amount to be deposited: "))
    savings.deposit(amount)
    print("Balance is: ", format(savings.get_balance(), ",.2f"), sep="")

    #Display the balance
    amount = float(input("Enter the amount to be withdrawn: "))
    savings.withdraw(amount)
    print("Balance is: ", format(savings.get_balance(), ",.2f"), sep="")

    print(savings)



main()