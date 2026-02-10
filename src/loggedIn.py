from account import Account
import util
from pathlib import Path


def logged_in(account: Account):
    print()
    while True:
        print(f"\nAccount@{account.Name}\n")
        print("a) Deposit")
        print("b) Withdraw")
        print("c) Balance")
        print("d) View Details")
        print("e) Change Details")
        print("f) Delete Account")
        print("g) Logout")
        print("h) Exit")
        choice = input("Enter your Choice: ")

        match choice:
            case 'a':
                amount = util.get_int("\nEnter Amount: ")
                if amount > 0:
                    account.Balance += amount
                    print(f"Account Balance: {amount}")
                else:
                    print("Invalid Amount!")
            case 'b':
                amount = util.get_int("\nEnter Amount: ")
                if amount <= account.Balance:
                    if amount > 0:
                        account.Balance -= amount
                        print(f"Account Balance: {amount}")
                    else:
                        print("Invalid Amount!")
                else:
                    print("Insufficient Balance!")
                    print(f"Account Balance: {amount}")
            case 'c':
                print(f"Balance: {account.Balance}")
            case 'd':
                print(f"\nName: {account.Name}")
                print(f"Date of Birth: {account.Birth}")
                print(f"Account Number: {account.Number}")
                print(f"Account Password: {account.Password}")
            case 'e':
                while True:
                    print("\na) Name")
                    print("b) Date of Birth")
                    print("c) Account Password")
                    print("d) Go Back")
                    choice2 = input("Enter your choice: ")

                    match choice2:
                        case 'a':
                            account.Name = Account.get_name()
                            print("Name Successfully changed!")
                        case 'b':
                            account.Birth = Account.get_birth()
                            print("Date of Birth Successfully changed!")
                        case 'c':
                            account.Password = Account.get_password()
                            print("Password Successfully changed!")
                        case 'd':
                            break
                        case _:
                            print("Invalid Choice!")
                            break
            case 'f':
                filepath = Path(Account.get_filename(account.Number))
                filepath.unlink()
                print("Account Deleted Successfully")
                break
            case 'g':
                account.write()
                break
            case 'h':
                account.write()
                exit(0)
            case _:
                print("Invalid Choice!")
