class InsufficientFundsError(Exception):
    pass


def check_balance():
    with open("account/balance.txt", "r") as file:
        balance = file.read()
        # will return my balance as a string, has trailing line break
        return balance


def deposit_funds(amount):
    # r+ means "read write mode"
    with open("account/balance.txt", "r+") as file:
        balance = file.read().strip()

        file.seek(0)  # Move the file pointer to the beginning
        file.write(str(int(balance) + amount))
        file.truncate()  # Truncate the file to the current file pointer (removes leftover content)
    print(f"\nYour available account balance is: ${check_balance()}")


def withdraw_funds(amount):
    balance = check_balance().strip()
    if amount > int(balance):
        raise InsufficientFundsError("\nYou need more money!")
    deposit_funds(-amount)
    print(f"\nYour available account balance is: ${check_balance()}")


def main():
    while True:
        print("""\nPlease choose from the available menu options:
    c - Check Balance
    d - Deposit Funds
    w - Withdraw Funds
    q - Quit
""")
        selection = input("> ")
        if selection == "c":
            print(f"\nYour available account balance is: ${check_balance()}")
        elif selection == "d":
            amount = input("\nEnter funds to deposit: ")
            deposit_funds(int(amount))
            print(f"\n${amount} deposited successfully.")
        elif selection == "w":
            amount = input("\nEnter funds to withdraw: ")
            try:
                withdraw_funds(int(amount))
            except InsufficientFundsError as e:
                print(e)
            # we only see the "else" if there ISN'T an error
            else:
                print(f"\n${amount} withdrawn successfully.")
            # all code runs the finally block
            # finally:
            #     print("error or not, this gets run.")
        elif selection == "q":
            print("\nSee you next time!")
            break
        else:
            print("\nPlease enter a valid choice.")


if __name__ == "__main__":
    main()
