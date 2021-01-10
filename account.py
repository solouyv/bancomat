#! /usr/bin/env python

import uuid
import random
from decimal import Decimal as Dec
from datetime import datetime


class Card:
    '''Класс карточка

    id - уникальный номер карточки
    passwd - пин-код доступа'''

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.passwd = '{0:0>4}'.format(random.randrange(0, 10000))

    def __repr__(self):
        return 'Card: {}'.format(self.id)


class Account:
    '''Класс счёт в банке

    number - уникальный номер для счёта
    amount - количество денег на счету
    history - история изменения счёта
    transaction - порядковый номер для очередной транзакции
    user - владелец счета
    card - карточка счета'''

    def __init__(self, name, number=uuid.uuid4(), amount='0.00', history={},
                 transaction=0):
        self.user = User(name)
        self.card = Card()
        self.number = number
        self.amount = Dec(amount)
        self.history = history
        self.transaction = transaction

    def __repr__(self):
        return ("Account: \n\t{}\n\tNumber {}"
                "\n\tPin {} \n\tAmount {} BYN").format(
                    self.user, self.number, self.card.passwd, self.amount)

    def get_history(self):
        '''Вывод истории изменения счёта'''

        for key in self.history:
            print(key, self.history[key])

    def sub_amount(self, address, ather):
        '''Метод для:
            - увеличения транзакции
            - записи транзакции в историю
            - вычитания суммы снатых наличных со счёта'''

        time = datetime.now()
        self.transaction += 1
        self.history[self.transaction] = "{} -- {} -- Withdrawn {} BYN".format(
                     address, time.strftime('%d-%m-%Y %H:%M:%S'), ather)
        self.amount -= Dec(ather)


class User:
    '''Класс пользователя

    name - имя пользователя
    и др. данные пользователя'''

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "User : {}".format(self.name)


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.card.id] = account

    def __repr__(self):
        return 'Bank: {}'.format(self.accounts)


if __name__ == "__main__":
    a = Account('Mike Doe', amount=100)
    b = Bank()
    b.add_account(a)
    print(b)
