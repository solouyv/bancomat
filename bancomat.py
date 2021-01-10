#!/usr/bin/env python

import uuid
from decimal import Decimal as Dec
from datetime import datetime

import console
from account import Account, Bank


class Bancomat:
    '''Класс банкомат

    bancomat_id - уникальный номер банкомата
    amount_money - количество денег в банкомате
    transaction - порядковый номер для транкзакций банкомата
    history - история операций в банкомате
    address - адресс установки банкомата
    '''

    def __init__(self, bancomat_id=str(uuid.uuid4()),
                 amount_money=Dec(1E+7), transaction=0, history={}):
        self.bancomat_id = bancomat_id
        self.amount_money = amount_money
        self.transaction = transaction
        self.history = history
        self.address = ''

    def __repr__(self):
        return 'Bancomat : {} \n\t{} -- {} BYN'.format(self.bancomat_id,
                                                       self.address,
                                                       self.amount_money)

    def authentication(self):
        '''Метод производящий аутентификацию'''

        attempt = 3
        input('Вставте карточку нажмите ок')
        # _card = card  # экземпляр обьекта Card будет считан с карточки
        _card = self.bank.accounts[list(self.bank.accounts.keys())[0]].card
        while attempt > 0:
            passwd = input('Введите пин-код: ')
            if _card.passwd == passwd:
                return _card.id
            else:
                attempt -= 1
                print('Осталось {} {}'.format(
                    attempt, 'попытки' if attempt > 1 else 'попытка'))
        return None

    def sub_amount(self, account,  other):
        '''Метод для:
            - увеличения номера транзакции
            - записи транзакции в историю
            - уменьшения количества наличных банкомата

        account - кто снимает деньги
        other - количесво снятых денег'''

        time = datetime.now()
        self.transaction += 1
        self.history[self.transaction] = "{} -- {} -- Withdrawn {} BYN".format(
            account.user.name, time.strftime('%d-%m-%Y %H:%M:%S'), other)
        self.amount_money -= Dec(other)

    def start(self, bank, address, money=None):
        '''Алгоритм работы банкомата'''

        self.address = address
        self.bank = bank
        if money:
            self.amount_money = money
        while True:
            card_id = self.authentication()
            if card_id:
                while True:
                    account = bank.accounts[card_id]
                    choice = console.get_choice()
                    if choice in 'Ww':
                        i = console.get_integer('How mach', minimum=5,
                                                allow_zero=False, default=5)
                        if account.amount >= i:
                            if self.amount_money >= i:
                                print('Take your maney.')
                                account.sub_amount(self.address, i)
                                self.sub_amount(account, i)
                            else:
                                print(self)
                        else:
                            print(account)
                    elif choice in 'Gg':
                        print(account)
                    elif choice in 'Ss':
                        account.get_history()
                    else:
                        break


if __name__ == '__main__':
    a = Account('Mike Doe', amount=100)
    print(a)
    c = Bank()
    c.add_account(a)
    print(c)
    b = Bancomat()
    print(b)
    b.start(c, 'Mogilev Jacubovskogo 66')
