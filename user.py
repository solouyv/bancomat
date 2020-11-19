#! /usr/bin/env python

class User:
    def __init__(self, name, password, account):
        self.name = name
        self.password = password
        self.account = str(account)

    def get_password(self):
        return self.password
    
    def get_account(self):
        return self.account
        
    def __repr__(self):
        return "{} {}".format(self.name, self.account)

if __name__ == '__main__':
    a = User('Jone', '#$%ErT%$#', 12345)
    print(a)
    for key in a.__dict__:
        print(key, a.__dict__[key])
    print(a.get_account())
    print(a.get_password())

