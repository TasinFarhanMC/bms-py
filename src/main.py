from account import Account
import login
from loggedIn import logged_in


def main():
    print("_______BANK_______")
    while True:
        print("\na) Create Account")
        print("b) Login")
        print("c) Exit")
        index = input("Enter your Choice: ")

        match index:
            case 'a':
                print()
                account = Account(Account.get_name(), Account.get_password(), Account.get_birth())
                print("\nAccount Successfully Created!")
                print(f"Account Number [DO NOT FORGET UNRECOVERABLE]: {account.Number}")
                account.write()
            case 'b':
                account = login.get_account()
                if account is None:
                    print("Account Docent Exist!")
                    continue
                if not login.check_password(account):
                    continue
                logged_in(account)
            case 'c':
                return
            case _:
                print("Invalid Choice!")


if __name__ == "__main__":
    main()
