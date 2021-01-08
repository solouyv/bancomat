#! /usr/bin/env pytho

import shelve
import uuid
from decimal import Decimal as Dec
from datetime import datetime


def save(func):
    '''
    декоратор для:
        - увеличения номера транзакции
        - сохранения операции в истории
        - сохранения состояния банкомата на диске

    '''
    def wraper(*arg, **kvarg):
        time = datetime.now()
        func(*arg, **kvarg)
        self_ = arg[0]
        self_.transaction += 1
        self_.history[self_.transaction] = (self_.bancomat_id, time.strftime(
            '%d-%m-%Y %H:%M:%S'), self_.amount_money)
        with shelve.open('bancomatdb') as db:
            db[self_.address] = self_
        return func
    return wraper


class Bancomat:
    def __init__(self, address, bancomat_id=str(uuid.uuid4()),
                 amount_money=Dec(1E+7), on_off='on',
                 transaction=0, history={}):
        self.bancomat_id = bancomat_id  # уникальный номер банкомата
        self.address = address  # адрес банкомата
        self.amount_money = amount_money  # количество денег в банкомате
        # при первом запуске
        self.on_off = on_off  # состояние включен выключен
        self.transaction = transaction  # номер операции банкомата
        self.history = history  # история операций банкомата

    def __repr__(self):
        return 'Bancomat : {} \n{} -- {} BYN'.format(self.bancomat_id,
                                                     self.address,
                                                     self.amount_money)

    @save
    def add_amount(self, ather):  # добавление денег в банкомат
        self.amount_money += Dec(ather)

    @save
    def sub_amount(self, ather):  # снятие денег из банкомата
        self.amount_money -= Dec(ather)

    def start(self):
        '''
        включение банкомата
        '''
        with shelve.open('bancomatdb') as db:
            a = db[self.address]
        a.on_off = "on"
        return a

    def stop(self):
        '''
        выключение банкомата с сохранением состояния на диске
        '''
        with shelve.open('bancomatdb') as db:
            self.on_off = "off"
            db[self.address] = self


if __name__ == '__main__':
    a = Bancomat('Mogilev Yacubovskogo 66')
    for key in a.history:
        print(key, a.history[key])
    print(a)
