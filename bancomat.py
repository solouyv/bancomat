#! /usr/bin/env python

import shelve
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
        self_ = arg[0] # присваивание переменной self_ первого атрибута метода класса self
        self_.transaction += 1
        self_.history[self_.transaction] = '-- {} -- Amount {} BYN'.format(
                       time.strftime('%d-%m-%Y %H:%M:%S'), self_.amount_money)
        with shelve.open('bancomatdb') as db:
            db[self_.address] = self_
        return func
    return wraper

class Bancomat:
    def __init__(self, address, amount_money=Dec(1E+7),
                ready=True, on_off='on', transaction=0, history={}):
        self.address = address # адрес банкомата
        self.ready = ready # готов ли к работе
        self.amount_money = amount_money + Dec('0.00') # количество денег в банкомате при первом запуске
        self.on_off = on_off # состояние включен выключен
        self.transaction = transaction # номер операции банкомата
        self.history = history # история операций банкомата

    def __repr__(self): # вывод остатка денег в банкомате (должен запускатся из банка)
        return 'Bancomat : {} -- {} BYN'.format(self.address,
                                                 self.amount_money)

    @save
    def add_amount(self, ather): # добавление денег в банкомат
        self.amount_money += Dec(str(ather))


    @save
    def sub_amount(self, ather): # снятие денег из банкомата
        self.amount_money -= Dec(str(ather))

    @staticmethod
    def start(address): # включение банкомата (из банка)
        with shelve.open('bancomatdb') as db:
            a = db[address]
        a.on_off = "on"
        return a

    def stop(self): # выключение банкомата с сохранением состояния на диске (из банка)
        with shelve.open('bancomatdb') as db:
            self.ready = False
            self.on_off = "off"
            db[self.address] = self



if __name__ == '__main__':
    a = Bancomat.start('Mogilev Yacubovskogo 66')
    for key in a.history:
        print(key, a.history[key])
    print(a)
