#! /usr/bin/env python


class Card:
    '''
    Класс карточка

    '''
    def __init__(self, id, passwd):
        self.id = id
        self.passwd = passwd


class User:
    '''
    Класс пользователя

    '''
    def __init__(self, name, id, passwd):
        self.name = name  # имя пользователя
        self.card = Card(id, passwd)

    def get_passwd(self):  # возвращает пароль к карточке
        return self.card.passwd

    def get_card_id(self):  # возвращает id карточки
        return self.card.id

    def __repr__(self):  # возращает данные пользователя
        return "User : {} {}".format(self.name, self.card.id)


if __name__ == '__main__':
    a = User('Jone', '1938479018734987', 12345)
    print(a)
    for key in a.__dict__:
        print(key, a.__dict__[key])
    print(a.get_card_id())
    print(a.get_passwd())
