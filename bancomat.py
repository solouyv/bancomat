#!/usr/bin/env python

import uuid
from decimal import Decimal as Dec
from datetime import datetime

from account import User, Card, Account


# def save(func):
#     '''
#     декоратор для:
#         - увеличения номера транзакции
#         - сохранения операции в истории
#         - сохранения состояния банкомата на диске

#     '''
#     def wraper(*arg, **kvarg):
#         time = datetime.now()
#         func(*arg, **kvarg)
#         self_ = arg[0]
#         self_.transaction += 1
#         self_.history[self_.transaction] = (self_.bancomat_id, time.strftime(
#             '%d-%m-%Y %H:%M:%S'), self_.amount_money)
#         with shelve.open('bancomatdb') as db:
#             db[self_.address] = self_
#         return func
#     return wraper


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
        print('Вставте карточку')
        _card = card  # экземпляр обьекта Card будет считан с карточки
        while attempt > 0:
            passwd = input('Введите пин-код')
            if _card.passwd == passwd:
                return _card.id
            else:
                attempt -= 1
                print('Осталось {} {}'.format(
                    attempt, 'попытки' if attempt > 1 else 'попытка'))
        return None

    def start(self, address, money=None):
        '''Включение банкомата'''
        self.address = address
        if money:
            self.amount_money = money
        card_id = self.authentication()
        if card_id:
            choice = get_choice()
        if choice in 'Ww':
            i = get_integer('How mach', minimum=5,
                                        allow_zero=False, default=5)
            if account.amount >= i:
                if bancomat.amount_money >=i:
                    print('Take your maney.')
                    account.sub_amount(i)
                    bancomat.sub_amount(i)
                else:
                    print(bancomat)
            else:
                print(account)
        elif choice in 'Cc':
            print('Put your money.')
            account.add_amount(5)
            bancomat.add_amount(5)
        elif choice in 'Gg':
            print(account)
        elif choice in 'Ss':
            account.get_history()
        else:
            break


if __name__ == '__main__':
    a = User('Mike Doe')
    a.get_card()
    print(a)
    a = Bancomat()
    a.start('Mogilev Jacubovskogo 66')
    print(a)
