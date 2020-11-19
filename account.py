#! /usr/bin/env python

from decimal import Decimal as dec
from datetime import datetime

class Account:
    def __init__(self, number, amount=dec('0.00'), history={}, transaction=0):
        self.number = number
        self.amount = amount
        self.history = history
        self.transaction = transaction

    def __repr__(self):
        return "Account # {} : {} BYN".format(self.number, self.amount )

    def get_amount(self):
        return self.amount

    def get_history(self):
        for key in self.history:
            print(key, self.history[key])

    def add_amount(self, ather):
        time = datetime.now()
        self.transaction += 1
        self.history[self.transaction] = "-- {} -- Credited {} BYN".format(
                                               time.strftime('%d-%m-%Y %H:%M:%S'), ather)
        self.amount += dec(str(ather))

    def sub_amount(self, ather):
        time = datetime.now()
        self.transaction += 1
        self.history[self.transaction] = "-- {} -- Withdrawn {} BYN".format(
                                               time.strftime('%d-%m-%Y %H:%M:%S'), ather)
        self.amount -= dec(str(ather))



if __name__ == "__main__":
    import time
    a = Account(12345)
    print(a.amount)
    a.add_amount(10.06)
    print(a.amount)
    time.sleep(1)
    a.sub_amount(5.03)
    print(a.amount)
    print(a)
    a.get_history()
