#! /usr/bin/env python
from decimal import Decimal as Dec

class Bancomat:
    def __init__(self, address, amount_money=Dec(1E+7), ready=True):
        self.address = address 
        self.ready = ready
        self.amount_money = amount_money + Dec('0.00')



if __name__ == '__main__':
    a = Bancomat('Yacubovskogo 66')
    for key in a.__dict__:
        print(key, a.__dict__[key])