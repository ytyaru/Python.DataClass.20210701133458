#!/usr/bin/env python3
# coding: utf8
# https://docs.python.org/ja/3.7/library/dataclasses.html
# https://docs.python.org/ja/3/library/stdtypes.html
from dataclasses import dataclass

@dataclass
class MyData:
    '''Class for keeping track of an item in inventory.'''
    name: str = ''
    data: bytes = b''
    age: int = 0
    rate: float = 0.0
    img: complex = 0.0
    is_dead: bool = False
    def intro(self) -> str: return f'My name is {self.name}.'


if __name__ == "__main__":
    d = MyData()
    d.name = 'Yamada'
    print(f"{d.name}, {d.age}")
    print(d.intro())

    d2 = MyData(age=99, name='Tanaka')
    print(d2.intro())
