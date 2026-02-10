from datetime import datetime, date
from random import randint
from pathlib import Path
from pickle import dump, load
import os
import sys

APP_NAME = "bms-py"


def get_data_dir() -> Path:
    if sys.platform.startswith("win"):
        base = Path(os.environ.get("APPDATA", Path.home()))
        path = base / f".{APP_NAME}"
    else:
        path = Path.home() / f".{APP_NAME}"
    path.mkdir(parents=True, exist_ok=True)
    return path


class Account:
    def __init__(self, name: str, password: str, date_of_birth: date):
        self.Name = name
        self.Password = password
        self.Birth = date_of_birth
        self.Balance = 0
        self.Number = randint(10000000, 99999999)

    def write(self):
        filename = Account.get_filename(self.Number)
        with open(filename, "wb") as file:
            dump(self, file)

    @staticmethod
    def get_name():
        name = input("Enter your Full Name: ")
        while ' ' not in name:
            name = input("Please Enter your Full Name: ")
        return name

    @staticmethod
    def get_password():
        password = input("Enter your password: ")
        while ' ' in password:
            password = input("\nPassword Cannot contain a Space!\nEnter your password: ")
        return password

    @staticmethod
    def get_birth():
        while True:
            try:
                date_str = input("Enter date of birth (YYYY-MM-DD): ")
                return datetime.strptime(date_str, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid Date!")
                print("Example: 2010-7-16\n")

    @staticmethod
    def get_number():
        while True:
            try:
                return int(input("Enter Account Number: "))
            except ValueError:
                print("Please Enter a Number!")

    @staticmethod
    def get_filename(number: int):
        num_str = str(number)
        name = str(int(num_str[-3:]) * number - int(num_str[-len(num_str) // 2:]))
        return get_data_dir() / name

    @staticmethod
    def read(number: int):
        filename = Account.get_filename(number)
        try:
            with open(filename, "rb") as file:
                return load(file)
        except FileNotFoundError:
            return None
