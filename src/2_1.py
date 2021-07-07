#!/usr/bin/env python3
# coding: utf8
class MyData:
    def __init__(self):
        self.__private_prop = 'private!!'


d = MyData()
print(d._MyData__private_prop)
print(d.__private_prop) # AttributeError: 'MyData' object has no attribute '__private_prop'

d.__x = 1 # OK。メンバを追加する
print(d.__x) # OK

