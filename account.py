#! /usr/bin/env python

from decimal import Decimal as dec

class account:

    def __init__(self, number, amount=dec(0), currency='BYN', history={}):
        self.number = number
        self.amount = amount
        self.currency = currency

    def get_amount(self, )
