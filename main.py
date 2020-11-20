#! /usr/bin/env python

from console import get_choice, get_integer, get_string
from bancomat import Bancomat
from account import Account
from user import User

account = Account(12345, '153')
accounts = {account.number : account}
bancomat = Bancomat.start('Mogilev Yacubovskogo 66')
user = User('John Doe', 12345, 123321)
users = {user.name : user}
connect_to_bank = True


if connect_to_bank:
    bancomat.ready = True

while bancomat.ready:
    who = get_string('Name', 'Name', default='John Doe')
    passw = get_integer('Passwd', 'Passwd', maximum=99999999, default=123321)
    if who in users and users[who].password == passw:
        account = accounts[users[who].account]
        while True:
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
    else:
        print('invalid!!')
        continue

