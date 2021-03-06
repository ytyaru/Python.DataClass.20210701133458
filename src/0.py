#!/usr/bin/env python3
# coding: utf8
# https://docs.python.org/ja/3.7/library/dataclasses.html
# https://docs.python.org/ja/3/library/stdtypes.html
from dataclasses import dataclass

@dataclass
class MyData:
    name: str
    age: int
    is_dead: bool
    def intro(self) -> str: return f'My name is {self.name}.'


if __name__ == "__main__":
    d = MyData('Yamada', 12, True)
    d.name = 'Tanaka'
    print(f"{d.name}, {d.age}")
    print(d.intro())
