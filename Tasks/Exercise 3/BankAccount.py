# main function?
import bank_class


def main():
    print("Hello!")
    # get the starting balance
    start_bal = float(input("Enter the starting balance: "))

    # create a BankAccount object
    savings = bank_class.BankAccount(start_bal)

    # Display the balance

    print("Balance is: ", format(savings.get_balance(), ",.2f"), sep="")
main()