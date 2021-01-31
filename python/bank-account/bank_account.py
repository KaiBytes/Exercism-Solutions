#learned about locking methods and raising errors

import threading

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.status = None
        self.lock = threading.Lock()

    def get_balance(self):
        if self.status == True:
            return self.balance
        else:
            raise ValueError("This account is closed! Balance does not exist.")

    def open(self):
        if self.status != True:
            self.status = True
            self.balance = 0
        else:
            raise ValueError("Account is already opened")

    def deposit(self, amount):
        self.lock.acquire()
        try:
            if self.status == True and amount > 0:
                self.balance += amount
            else:
                raise ValueError("You cannot deposit a negative amount!")
        finally:
            self.lock.release()

    def withdraw(self, amount):
        self.lock.acquire()
        try:
            if self.status == True and amount <= self.balance and amount > 0:
                self.balance -= amount
            else:
                raise ValueError("You do not have that kind of money!")
        finally:
            self.lock.release()

    def close(self):
        if self.status == True:
            self.status = False
        else:
            raise ValueError("Account is already closed")

