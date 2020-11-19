#! /usr/bin/env python

class User:

    def __init__(self, name, password):
        self.name = name
        self.code = password

    def get_password(self):
        return self.password
