import sqlite3
import random

class Account:
    def __init__(self, name, num, bal):
        self.number = num
        self.balance = bal
        self.name = name

def main():
    print("\nWelcome to Bank of Pilani\n\nPress 1 to create an account\nPress 2 to deposit money in your account\nPress 3 to withdraw money from your account\nPress 4 to view your account summary\nPress 5 to exit\n")
    while True:
        try:
            task = int(input())
            if (task < 1) or (task > 5):
                print("Check your input!")
            else:
                break
        except ValueError:
            print("Check your input!")

    if task == 5:
        print("Thank You!")
        exit()

    connection = sqlite3.connect("account.db")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS accounts
                   (Name TEXT, Account_Number INTEGER PRIMARY KEY, Balance INTEGER ) """)

    connection.commit()

    if task == 1:
        name = input("Please enter your name: ")
        account = Account(name, random.randint(100000000000, 999999999999), 0)
        cursor.execute("INSERT INTO accounts VALUES(?, ?, ?)",(account.name, account.number, 0))
        connection.commit()
        print(f"Hi {account.name}!\nYour account has been created!\nYour account number is: {account.number}\nYour starting balance is Rs 0\n")
        connection.close()
        exit()

    acc_no = [int(input("Please enter your account number: "))]
    cursor.execute("SELECT * FROM accounts WHERE Account_Number = (?)",(acc_no))
    info = cursor.fetchall()
    if info == []:
        print("Account not found!")
        connection.close()
        exit()

    if task == 2:
        while True:
            try:
                money = int(input("Please enter the amount you would like to deposit: "))
                if money < 0 :
                    print("Check your input!")
                else:
                    break
            except ValueError:
                print("Check your input!")

        cursor.execute("update accounts set balance=balance+(?) where account_number=(?)", (money,acc_no[0]))
        connection.commit()
        print(f"Rs {money} has successfully been added to your balance\nYour current account balance is {info[0][2] + money}")

    if task == 3:
        while True:
            try:
                money = int(input("Please enter the amount you would like to withdraw: "))
                if money < 0 :
                    print("Check your input!")
                if money > info[0][2]:
                    print("Insufficient balance!")
                else:
                    break
            except ValueError:
                print("Check your input!")
        cursor.execute("update accounts set balance=balance-(?) where account_number=(?)", (money,acc_no[0]))
        print(f"Rs {money} has successfully been withdrawn from your account\nYour current account balance is {info[0][2] - money}")

    if task==4:
        print(f"Name: {info[0][0]}\nAccount Number: {info[0][1]}\nAccount Balance: Rs {info[0][2]}")

    connection.commit()
    connection.close()

if __name__ == "__main__":
    main()
