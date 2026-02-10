from account import Account
import util


def check_password(account: Account):
    while account.Password != input("Enter Account Password: "):
        print("Incorrect Password!\n")
        print("a) Retry")
        print("b) Go to home")
        choice = input("Enter your Choice: ")

        match choice:
            case 'a':
                continue
            case 'b':
                return False
            case _:
                print("Invalid Choice!")
                return False

    return True


def get_account():
    acc_num = util.get_int("Enter Account Number: ")
    return Account.read(acc_num)
