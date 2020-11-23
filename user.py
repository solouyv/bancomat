#! /usr/bin/env python

class User:
    '''
    Класс пользователя

    '''
    def __init__(self, name, account, password):
        self.name = name # имя пользователя
        self.password = password # пароль доступа к счёту
        self.account = account # номер счёта

    def get_password(self): # возвращает пароль к счёту
        return self.password

    def get_account(self): # возвращает номер счёта
        return self.account

    def __repr__(self): # возращает данные пользователя
        return "User : {} {}".format(self.name, self.account)

if __name__ == '__main__':
    a = User('Jone', '#$%ErT%$#', 12345)
    print(a)
    for key in a.__dict__:
        print(key, a.__dict__[key])
    print(a.get_account())
    print(a.get_password())

