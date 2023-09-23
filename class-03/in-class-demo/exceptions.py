# print(3/0)
# raise Exception("new message")


try:
    print(3/0)
except IndexError:
    print("that index doesn't exist")
except TypeError:
    print("incompatible types.")
except ZeroDivisionError as e:
    print("You tried to divide by zero!!!!")
    print(e)
except Exception as e:
    print(e)


print("script continues")


try:
    "a" + 1
except TypeError:
    print("Incompatible types.")


my_list = [1, 2, 3, 4, 5]

try:
    print(my_list[7])
except IndexError:
    print("that index doesn't exist!")


class InsufficientFundsError(Exception):
    pass


def withdraw(account_balance, amount):
    if amount > account_balance:
        raise InsufficientFundsError
    return account_balance - amount


print(withdraw(20, 21))
