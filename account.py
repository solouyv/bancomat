#! /usr/bin/env python

from decimal import Decimal as Dec
from datetime import datetime


class Account:
    '''
    класс описывает поведение счёта в банке

    '''
    def __init__(self, number, amount='0.00', history={},
                 transaction=0):
        self.number = number  # номер счета
        self.amount = Dec(amount)  # количество денег на счету
        self.history = history  # история изменения счета
        self.transaction = transaction  # номер транзакции (их количество)

    def __repr__(self):
        return "Account # {} : {} BYN".format(self.number, self.amount)
        # вывод информации счета

    def get_amount(self):  # вывод остатка счета
        return self.amount

    def get_history(self):  # вывод истории транзакций
        for key in self.history:
            print(key, self.history[key])

    def add_amount(self, ather):  # добавление денег на счёт
        time = datetime.now()
        self.transaction += 1  # номер транзакции
        self.history[self.transaction] = "-- {} -- Credited {} BYN".format(
                     time.strftime('%d-%m-%Y %H:%M:%S'), ather)
        # добавление транзакции в историю счёта
        self.amount += Dec(str(ather))  # добавление денег на счёт

    def sub_amount(self, ather):  # снятие денег со счёта ()
        time = datetime.now()
        self.transaction += 1
        self.history[self.transaction] = "-- {} -- Withdrawn {} BYN".format(
                     time.strftime('%d-%m-%Y %H:%M:%S'), ather)
        self.amount -= Dec(str(ather))


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
