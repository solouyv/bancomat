#! /usr/bin/env python

import uuid
import random
from decimal import Decimal as Dec


class Card:
    r'''Класс карточка

    id - уникальный номер карточки
    passwd - пин-код доступа
    '''
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.passwd = '{0:0>4}'.format(random.randrange(0, 10000))

    def __repr__(self):
        return 'Card: {}'.format(self.id)


class Account:
    r'''Класс счёт в банке

    number - уникальный номер для счёта
    amount - количество денег на счету
    history - история изменения счёта
    transaction - порядковый номер для очередной транзакции
    '''
    def __init__(self, number=uuid.uuid4(), amount='0.00', history={},
                 transaction=0):
        self.number = number
        self.amount = Dec(amount)
        self.history = history
        self.transaction = transaction

    def __repr__(self):
        return "Account: {} : {} BYN".format(self.number, self.amount)

    def issue_card(self):
        '''Выпуск карточки по запросу пользователя

        card - экземпляр о карточка
        '''
        self.card = Card()
        return self.card

    # def get_amount(self):
    #     '''Вывод текущего остатка счёта'''
    #     return self.amount

    # def get_history(self):  # вывод истории транзакций
    #     for key in self.history:
    #         print(key, self.history[key])

    # def add_amount(self, ather):  # добавление денег на счёт
    #     time = datetime.now()
    #     self.transaction += 1  # номер транзакции
    #     self.history[self.transaction] = "-- {} -- Credited {} BYN".format(
    #                  time.strftime('%d-%m-%Y %H:%M:%S'), ather)
    #     # добавление транзакции в историю счёта
    #     self.amount += Dec(str(ather))  # добавление денег на счёт

    # def sub_amount(self, ather):  # снятие денег со счёта ()
    #     time = datetime.now()
    #     self.transaction += 1
    #     self.history[self.transaction] = "-- {} -- Withdrawn {} BYN".format(
    #                  time.strftime('%d-%m-%Y %H:%M:%S'), ather)
    #     self.amount -= Dec(str(ather))


class User:
    '''Класс пользователя

    name - имя пользователя
    account - экземпляр обьекта счёт в банке
    '''
    def __init__(self, name):
        self.name = name
        self.account = Account()

    def get_card(self):
        '''Получение карточки к счёту'''
        self.card = self.account.issue_card()

    def __repr__(self):
        return "User : \n\tName: {}\n\t{}\n\t{}".format(
            self.name, self.account, self.card)


if __name__ == "__main__":
    a = User('Mike Doe')
    a.get_card()
    print(a)
